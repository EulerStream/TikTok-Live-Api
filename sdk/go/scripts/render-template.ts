import * as fs from 'fs';
import * as path from 'path';

const GENERATED_DIR: string = path.resolve(__dirname, '..', 'generated');
const TEMPLATE_PATH: string = path.resolve(__dirname, '..', 'client.go.template');
const OUTPUT_PATH: string = path.resolve(__dirname, '..', 'client.go');
const OVERRIDES_PATH: string = path.resolve(__dirname, '..', 'overrides.json');

// Discover all *APIService types from generated Go files
const apiFiles: string[] = fs.readdirSync(GENERATED_DIR).filter((f: string) => f.startsWith('api_') && f.endsWith('.go'));
const serviceTypes: string[] = [];

const serviceRegex = /type (\w+APIService) service/g;
for (const file of apiFiles) {
    const content: string = fs.readFileSync(path.join(GENERATED_DIR, file), 'utf-8');
    let match: RegExpExecArray | null;
    while ((match = serviceRegex.exec(content)) !== null) {
        serviceTypes.push(match[1]);
    }
    serviceRegex.lastIndex = 0;
}

if (serviceTypes.length === 0) {
    console.error('No API service types found in generated Go SDK.');
    process.exit(1);
}

// Sort for deterministic output
serviceTypes.sort();

// Load overrides for custom field names (PascalCase for Go exported fields)
const overrides: Record<string, string> = fs.existsSync(OVERRIDES_PATH)
    ? JSON.parse(fs.readFileSync(OVERRIDES_PATH, 'utf-8'))
    : {};

// Derive the exported Go field name from service type
function toFieldName(serviceType: string): string {
    const apiFieldName: string = serviceType.replace(/Service$/, '');
    if (overrides[apiFieldName]) return overrides[apiFieldName];
    // Normalize the "LIVE" acronym to "Live" so unoverridden names read naturally
    // (e.g. TikTokLIVERoomsAPI -> TikTokLiveRooms, not TikTokLIVERooms).
    return apiFieldName.replace(/API$/, '').replace(/LIVE/g, 'Live');
}

// Build entries
const entries = serviceTypes.map((svc: string) => ({
    serviceType: svc,
    generatedField: svc.replace(/Service$/, ''),
    fieldName: toFieldName(svc),
}));

// Build template replacements
const properties: string = entries
    .map(e => `${e.fieldName} *eulerapi.${e.serviceType}`)
    .join('\n\t');

const constructors: string = entries
    .map(e => `${e.fieldName}: raw.${e.generatedField},`)
    .join('\n\t\t');

// Render template
let template: string = fs.readFileSync(TEMPLATE_PATH, 'utf-8');
template = template.replace('{{API_PROPERTIES}}', properties);
template = template.replace('{{API_CONSTRUCTORS}}', constructors);

fs.writeFileSync(OUTPUT_PATH, template, 'utf-8');
console.log(`Generated ${OUTPUT_PATH} with ${entries.length} API services:`);
entries.forEach(e => console.log(`  ${e.serviceType} -> ${e.fieldName} (from raw.${e.generatedField})`));
