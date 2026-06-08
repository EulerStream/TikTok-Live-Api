import * as fs from 'fs';
import * as path from 'path';

const SDK_API_DIR = path.resolve(__dirname, '..', 'src/generated/src/EulerApiSdk/Api');
const TEMPLATE_PATH = path.resolve(__dirname, '..', 'src/EulerStreamApiClient.cs.template');
const OUTPUT_PATH = path.resolve(__dirname, '..', 'src/generated/src/EulerApiSdk/EulerStreamApiClient.cs');
const OVERRIDES_PATH = path.resolve(__dirname, '..', 'overrides.json');

// Discover all *Api classes from generated SDK directory
// Each file in the Api folder that matches *Api.cs (excluding IApi.cs) contains an API class
const apiFiles = fs.readdirSync(SDK_API_DIR)
    .filter(f => f.endsWith('Api.cs') && !f.startsWith('I'));

const apiClasses: string[] = [];
for (const file of apiFiles) {
    const filePath = path.join(SDK_API_DIR, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const matches = Array.from(content.matchAll(/public sealed partial class (\w+Api)\s*:/g));
    for (const match of matches) {
        apiClasses.push(match[1]);
    }
}

if (apiClasses.length === 0) {
    console.error('No API classes found in generated SDK.');
    process.exit(1);
}

// Load overrides for custom property names
const overrides: Record<string, string> = fs.existsSync(OVERRIDES_PATH)
    ? JSON.parse(fs.readFileSync(OVERRIDES_PATH, 'utf-8'))
    : {};

// Derive property name: use override, or strip "Api" and keep PascalCase
function toPropertyName(className: string): string {
    if (overrides[className]) return overrides[className];
    // Normalize the "LIVE" acronym to "Live" so unoverridden names read naturally
    // (e.g. TikTokLIVERoomsApi -> TikTokLiveRooms, not TikTokLIVERooms).
    return className.replace(/Api$/, '').replace(/LIVE/g, 'Live');
}

// Build replacements
const entries = apiClasses.map(cls => ({
    className: cls,
    interfaceName: `I${cls}`,
    propName: toPropertyName(cls),
}));

const properties = entries
    .map(e => `        /// <summary>\n        /// ${e.propName} API group.\n        /// </summary>\n        public ${e.interfaceName} ${e.propName} { get; }`)
    .join('\n\n');

const constructors = entries
    .map(e => `            ${e.propName} = _serviceProvider.GetRequiredService<${e.interfaceName}>();`)
    .join('\n');

// Render template
let template = fs.readFileSync(TEMPLATE_PATH, 'utf-8');
template = template.replace('{{API_PROPERTIES}}', properties);
template = template.replace('{{API_CONSTRUCTORS}}', constructors);

fs.writeFileSync(OUTPUT_PATH, template, 'utf-8');
console.log(`Generated ${OUTPUT_PATH} with ${entries.length} API classes:`);
entries.forEach(e => console.log(`  ${e.className} -> ${e.propName}`));
