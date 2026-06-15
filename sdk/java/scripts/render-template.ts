import * as fs from 'fs';
import * as path from 'path';

const SDK_API_DIR = path.resolve(__dirname, '..', 'src/generated/src/main/java/com/eulerstream/api');
const TEMPLATE_PATH = path.resolve(__dirname, '..', 'src/EulerStreamApiClient.java.template');
const OUTPUT_PATH = path.resolve(__dirname, '..', 'src/generated/src/main/java/com/eulerstream/EulerStreamApiClient.java');
const OVERRIDES_PATH = path.resolve(__dirname, '..', 'overrides.json');

// Discover all *Api classes from generated SDK directory
const apiFiles = fs.readdirSync(SDK_API_DIR)
    .filter(f => f.endsWith('Api.java'))
    .map(f => f.replace('.java', ''));

if (apiFiles.length === 0) {
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
const entries = apiFiles.map(cls => ({
    className: cls,
    propName: toPropertyName(cls),
}));

const imports = entries
    .map(e => `import com.eulerstream.api.${e.className};`)
    .join('\n');

const fields = entries
    .map(e => `    private final ${e.className} ${e.propName};`)
    .join('\n');

const constructors = entries
    .map(e => `        this.${e.propName} = new ${e.className}(apiClient);`)
    .join('\n');

const getters = entries
    .map(e => {
        const methodName = e.propName;
        return [
            `    /**`,
            `     * Get the ${e.className} instance.`,
            `     *`,
            `     * @return the ${e.className}`,
            `     */`,
            `    public ${e.className} ${methodName}() {`,
            `        return ${e.propName};`,
            `    }`,
        ].join('\n');
    })
    .join('\n\n');

// Render template
let template = fs.readFileSync(TEMPLATE_PATH, 'utf-8');
template = template.replace('{{API_IMPORTS}}', imports);
template = template.replace('{{API_FIELDS}}', fields);
template = template.replace('{{API_CONSTRUCTORS}}', constructors);
template = template.replace('{{API_GETTERS}}', getters);

fs.writeFileSync(OUTPUT_PATH, template, 'utf-8');
console.log(`Generated ${OUTPUT_PATH} with ${entries.length} API classes:`);
entries.forEach(e => console.log(`  ${e.className} -> ${e.propName}`));
