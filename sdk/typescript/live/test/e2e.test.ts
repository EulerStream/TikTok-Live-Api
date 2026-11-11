import assert from "node:assert";
import TikTokLiveApiSdk from "../src/index.js";

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
    console.log("\n--- E2E: TikTokLiveApiSdk tests ---\n");

    const client = new TikTokLiveApiSdk();

    // CI has no secrets, so this must be a route that answers without an API
    // key. The TikTok LIVE routes do, but only a few times a minute per IP, so
    // they return 429 on a busy runner. The rate-limit route reports those
    // limits and is not itself subject to them.
    await test("getRateLimits returns status 200", async () => {
        const response = await client.accounts.getRateLimits();
        assert.strictEqual(response.status, 200, `expected status 200, got ${response.status}`);
    });

    await test("getRateLimits returns the daily limit", async () => {
        const response = await client.accounts.getRateLimits();
        assert.ok(typeof response.data.day?.max === "number", "response.data.day.max should be a number");
    });

    // Summary
    console.log(`\n--- Results: ${passed} passed, ${failed} failed ---\n`);

    if (failed > 0) {
        process.exit(1);
    }
})();
