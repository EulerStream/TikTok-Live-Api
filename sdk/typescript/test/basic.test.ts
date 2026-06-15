import assert from "node:assert";
import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";
import EulerStreamApiClient, { buildConfig } from "../src/index.js";
import * as Sdk from "../src/sdk/index.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// The API surface is determined dynamically at codegen time: render-template.ts
// discovers every *Api class from the generated SDK (itself produced from the
// live OpenAPI spec) and writes test/sdk-manifest.json. The tests below assert
// against that manifest so they never go stale when the spec adds, renames, or
// removes API groups.
const MANIFEST_PATH = path.resolve(__dirname, "sdk-manifest.json");

interface ApiEntry {
    className: string;
    propName: string;
}

function loadManifest(): ApiEntry[] {
    if (!fs.existsSync(MANIFEST_PATH)) {
        throw new Error(
            `Manifest not found at ${MANIFEST_PATH}. Run codegen ('pnpm generate') first.`,
        );
    }
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, "utf-8"));
    if (!Array.isArray(manifest.apis) || manifest.apis.length === 0) {
        throw new Error(`Manifest at ${MANIFEST_PATH} contains no API entries.`);
    }
    return manifest.apis as ApiEntry[];
}

const apiEntries = loadManifest();

let passed = 0;
let failed = 0;

function test(name: string, fn: () => void): void {
    try {
        fn();
        console.log(`  PASS: ${name}`);
        passed++;
    } catch (err: any) {
        console.error(`  FAIL: ${name}`);
        console.error(`        ${err.message}`);
        failed++;
    }
}

console.log("\n--- EulerStreamApiClient tests ---\n");

// 1. Can be instantiated with no arguments
test("EulerStreamApiClient can be instantiated with no arguments", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client, "client should be truthy");
});

// 2. Every API group from the manifest is exported by the generated SDK and
//    exposed on the client as an instance of its API class.
for (const { className, propName } of apiEntries) {
    test(`SDK exports ${className}`, () => {
        const ApiClass = (Sdk as Record<string, unknown>)[className];
        assert.ok(
            typeof ApiClass === "function",
            `generated SDK should export a ${className} class`,
        );
    });

    test(`client.${propName} is a ${className} instance`, () => {
        const ApiClass = (Sdk as Record<string, unknown>)[className] as (new (...args: any[]) => object);
        const client = new EulerStreamApiClient();
        const instance = (client as Record<string, unknown>)[propName];
        assert.ok(
            instance instanceof ApiClass,
            `client.${propName} should be a ${className} instance`,
        );
    });
}

// 3. Client exposes the configuration property
test("client exposes configuration property", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.configuration !== undefined, "configuration should be defined");
    assert.ok(typeof client.configuration === "object", "configuration should be an object");
});

// 4. buildConfig returns correct defaults
console.log("\n--- buildConfig tests ---\n");

test("buildConfig returns default basePath", () => {
    const config = buildConfig({});
    assert.strictEqual(config.basePath, "https://api.eulerstream.com");
});

test("buildConfig returns baseOptions with validateStatus", () => {
    const config = buildConfig({});
    assert.ok(config.baseOptions, "baseOptions should be defined");
    assert.ok(typeof config.baseOptions.validateStatus === "function", "validateStatus should be a function");
    assert.strictEqual(config.baseOptions.validateStatus(404), true, "validateStatus should always return true");
    assert.strictEqual(config.baseOptions.validateStatus(500), true, "validateStatus should always return true");
});

test("buildConfig returns isJsonMime function", () => {
    const config = buildConfig({});
    assert.ok(typeof config.isJsonMime === "function", "isJsonMime should be a function");
    assert.strictEqual(config.isJsonMime("application/json"), true);
    assert.strictEqual(config.isJsonMime("text/html"), false);
});

test("buildConfig allows overriding basePath", () => {
    const config = buildConfig({ basePath: "https://custom.example.com" });
    assert.strictEqual(config.basePath, "https://custom.example.com");
});

// 5. Configuration with a custom apiKey
test("buildConfig sets X-Api-Key header when apiKey is provided", () => {
    const config = buildConfig({ apiKey: "my-test-key-123" });
    assert.ok(config.baseOptions, "baseOptions should be defined");
    assert.ok(config.baseOptions.headers, "headers should be defined");
    assert.strictEqual(config.baseOptions.headers["X-Api-Key"], "my-test-key-123");
});

test("buildConfig removes apiKey from config after setting header", () => {
    const config = buildConfig({ apiKey: "my-test-key-123" });
    assert.strictEqual(config.apiKey, undefined, "apiKey should be removed from config");
});

test("buildConfig does not set X-Api-Key header when apiKey is absent", () => {
    const config = buildConfig({});
    assert.ok(config.baseOptions, "baseOptions should be defined");
    const xApiKey = config.baseOptions.headers?.["X-Api-Key"];
    assert.strictEqual(xApiKey, undefined, "X-Api-Key header should not be set");
});

// 6. Client constructed with apiKey passes it through to configuration
test("EulerStreamApiClient passes apiKey through to configuration headers", () => {
    const client = new EulerStreamApiClient({ apiKey: "sdk-key-456" });
    assert.strictEqual(
        client.configuration.baseOptions?.headers?.["X-Api-Key"],
        "sdk-key-456",
    );
});

// Summary
console.log(`\n--- Results: ${passed} passed, ${failed} failed ---\n`);

if (failed > 0) {
    process.exit(1);
}
