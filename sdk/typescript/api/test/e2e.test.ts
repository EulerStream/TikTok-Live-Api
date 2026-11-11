import assert from "node:assert";
import TikTokApiSdk from "../src/index.js";

let passed = 0;
let failed = 0;

async function test(name: string, fn: () => Promise<void>): Promise<void> {
    try {
        await fn();
        console.log(`  PASS: ${name}`);
        passed++;
    } catch (err: any) {
        console.error(`  FAIL: ${name}`);
        console.error(`        ${err.message}`);
        failed++;
    }
}

(async () => {
    console.log("\n--- E2E: TikTokApiSdk tests ---\n");

    const client = new TikTokApiSdk();

    await test("getHosts returns status 200", async () => {
        const response = await client.analytics.getHosts();
        assert.strictEqual(response.status, 200, `expected status 200, got ${response.status}`);
    });

    await test("getHosts returns data with hosts array", async () => {
        const response = await client.analytics.getHosts();
        assert.ok(typeof response.data === "object" && response.data !== null, "response.data should be an object");
        assert.ok(Array.isArray(response.data.hosts), "response.data.hosts should be an array");
    });

    // Summary
    console.log(`\n--- Results: ${passed} passed, ${failed} failed ---\n`);

    if (failed > 0) {
        process.exit(1);
    }
})();
