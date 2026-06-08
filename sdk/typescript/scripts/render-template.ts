import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const SDK_API_PATH = path.resolve(__dirname, '..', 'src/sdk/api.ts');
const TEMPLATE_PATH = path.resolve(__dirname, '..', 'src/index.ts.template');
const OUTPUT_PATH = path.resolve(__dirname, '..', 'src/index.ts');
const OVERRIDES_PATH = path.resolve(__dirname, '..', 'overrides.json');
const MANIFEST_PATH = path.resolve(__dirname, '..', 'test/sdk-manifest.json');

// Discover all *Api classes from generated SDK
const apiSource = fs.readFileSync(SDK_API_PATH, 'utf-8');
const apiClasses = Array.from(apiSource.matchAll(/export class (\w+Api) extends BaseAPI/g))
    .map(m => m[1]);

if (apiClasses.length === 0) {
    console.error('No API classes found in generated SDK.');
    process.exit(1);
}

// Load overrides for custom property names
const overrides: Record<string, string> = fs.existsSync(OVERRIDES_PATH)
    ? JSON.parse(fs.readFileSync(OVERRIDES_PATH, 'utf-8'))
    : {};

// Derive property name: use override, or strip "Api" and lower-first
function toPropertyName(className: string): string {
    if (overrides[className]) return overrides[className];
    // Normalize the "LIVE" acronym to "Live" so unoverridden names read naturally
    // (e.g. TikTokLIVERoomsApi -> tikTokLiveRooms, not tikTokLIVERooms).
    const stripped = className.replace(/Api$/, '').replace(/LIVE/g, 'Live');
    return stripped.charAt(0).toLowerCase() + stripped.slice(1);
}

// Build replacements
const entries = apiClasses.map(cls => ({
    className: cls,
    propName: toPropertyName(cls),
}));

const imports = entries.map(e => e.className).join(',\n  ');
const properties = entries.map(e => `public readonly ${e.propName}: ${e.className};`).join('\n  ');
const constructors = entries.map(e => `this.${e.propName} = new ${e.className}(this.configuration);`).join('\n    ');

// Render template
let template = fs.readFileSync(TEMPLATE_PATH, 'utf-8');
template = template.replace('{{API_IMPORTS}}', imports);
template = template.replace('{{API_PROPERTIES}}', properties);
template = template.replace('{{API_CONSTRUCTORS}}', constructors);

fs.writeFileSync(OUTPUT_PATH, template, 'utf-8');
console.log(`Generated ${OUTPUT_PATH} with ${entries.length} API classes:`);
entries.forEach(e => console.log(`  ${e.className} -> ${e.propName}`));

// Emit a manifest of the discovered API surface so tests can assert against
// the generated SDK dynamically instead of hardcoding class/property names.
// The generated SDK is the live OpenAPI spec realized through the generator,
// so this manifest stays in sync with the spec automatically.
fs.mkdirSync(path.dirname(MANIFEST_PATH), { recursive: true });
fs.writeFileSync(MANIFEST_PATH, JSON.stringify({ apis: entries }, null, 2) + '\n', 'utf-8');
console.log(`Wrote manifest ${MANIFEST_PATH}`);
