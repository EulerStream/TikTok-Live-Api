import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const COMMON_DIR = path.resolve(__dirname, '..');
const TEMPLATE_PATH = path.join(COMMON_DIR, 'index.ts.template');
const OVERRIDES_PATH = path.join(COMMON_DIR, 'overrides.json');

/**
 * Render a package's client wrapper from the shared template.
 *
 * Reads the API classes the generator emitted into `<packageDir>/src/sdk`,
 * writes `<packageDir>/src/index.ts` with one client property per class, and
 * writes `<packageDir>/test/sdk-manifest.json` for the tests.
 *
 * @param packageDir The package folder, e.g. `sdk/typescript/live`
 * @param clientClass The name the client class is exported under
 */
export function renderTemplate(packageDir: string, clientClass: string): void {
    const sdkApiPath = path.join(packageDir, 'src/sdk/api.ts');
    const outputPath = path.join(packageDir, 'src/index.ts');
    const manifestPath = path.join(packageDir, 'test/sdk-manifest.json');

    // Discover all *Api classes from generated SDK
    const apiSource = fs.readFileSync(sdkApiPath, 'utf-8');
    const apiClasses = Array.from(apiSource.matchAll(/export class (\w+Api) extends BaseAPI/g))
        .map(m => m[1]);

    if (apiClasses.length === 0) {
        throw new Error(`No API classes found in generated SDK at ${sdkApiPath}.`);
    }

    // Load overrides for custom property names. The file is shared by every
    // package, so it may name classes this package's spec does not contain.
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
    template = template.replaceAll('{{CLIENT_CLASS}}', clientClass);

    fs.writeFileSync(outputPath, template, 'utf-8');
    console.log(`Generated ${outputPath} as ${clientClass} with ${entries.length} API classes:`);
    entries.forEach(e => console.log(`  ${e.className} -> ${e.propName}`));

    // Emit a manifest of the discovered API surface so tests can assert against
    // the generated SDK dynamically instead of hardcoding class/property names.
    // The generated SDK is the OpenAPI spec realized through the generator,
    // so this manifest stays in sync with the spec automatically.
    fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
    fs.writeFileSync(manifestPath, JSON.stringify({ apis: entries }, null, 2) + '\n', 'utf-8');
    console.log(`Wrote manifest ${manifestPath}`);
}
