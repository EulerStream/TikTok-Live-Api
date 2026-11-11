import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { renderTemplate } from './render-template.js';

/**
 * Generate one TypeScript SDK package from the committed OpenAPI spec.
 *
 * Run from the package folder (`pnpm run generate` does this). The folder's
 * sdk.json says what to build:
 *
 *   { "clientClass": "TikTokLiveApiSdk", "specPackage": "live" }
 *
 * `clientClass` names the exported client. `specPackage`, when present, is a
 * key in spec/packages.json: the spec is cut down to that package's tags
 * before generation. Without it the package gets the full spec.
 *
 * Everything this writes (src/, openapitools.json, test/sdk-manifest.json) is
 * git-ignored build output; CI runs the same script.
 */

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const COMMON_DIR = path.resolve(__dirname, '..');
const REPO_ROOT = path.resolve(COMMON_DIR, '..', '..', '..');
const SPEC_PATH = path.join(REPO_ROOT, 'spec', 'openapi.json');
const PACKAGES_PATH = path.join(REPO_ROOT, 'spec', 'packages.json');
const SPEC_SCRIPTS_DIR = path.join(REPO_ROOT, '.github', 'scripts');

interface SdkConfig {
    clientClass: string;
    specPackage?: string;
}

const packageDir = process.cwd();
const configPath = path.join(packageDir, 'sdk.json');

if (!fs.existsSync(configPath)) {
    throw new Error(`No sdk.json in ${packageDir}. Run this from an SDK package folder.`);
}

const config: SdkConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));

if (!/^[A-Za-z_$][\w$]*$/.test(config.clientClass ?? '')) {
    throw new Error(`${configPath}: "clientClass" must be a valid class name, got ${JSON.stringify(config.clientClass)}.`);
}

function run(command: string, args: string[]): void {
    execFileSync(command, args, { cwd: packageDir, stdio: 'inherit' });
}

// 1. Spec: copy, normalize, and cut down to this package's tags if it has any.
const buildDir = path.join(packageDir, 'build');
const buildSpec = path.join(buildDir, 'openapi.json');
fs.mkdirSync(buildDir, { recursive: true });
fs.copyFileSync(SPEC_PATH, buildSpec);
run('python3', [path.join(SPEC_SCRIPTS_DIR, 'normalize_spec.py'), buildSpec]);
if (config.specPackage) {
    run('python3', [path.join(SPEC_SCRIPTS_DIR, 'filter_spec.py'), buildSpec, PACKAGES_PATH, config.specPackage]);
}

// 2. Generate. openapi-generator-cli reads its version pin from the working
//    directory, so the shared pin is copied in.
fs.copyFileSync(path.join(COMMON_DIR, 'openapitools.json'), path.join(packageDir, 'openapitools.json'));
const srcDir = path.join(packageDir, 'src');
fs.rmSync(srcDir, { recursive: true, force: true });
run('npx', ['openapi-generator-cli', 'generate', '-i', buildSpec, '-g', 'typescript-axios', '-o', path.join(srcDir, 'sdk')]);

// 3. Shared hand-written sources and the client wrapper.
fs.copyFileSync(path.join(COMMON_DIR, 'utils.ts'), path.join(srcDir, 'utils.ts'));
renderTemplate(packageDir, config.clientClass);
