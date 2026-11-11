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

    // The hashtag list is a TikTok LIVE route that answers without an API key,
    // which CI needs: the test workflow has no secrets.
    await test("retrieveHashtagList returns status 200", async () => {
        const response = await client.webcast.retrieveHashtagList();
        assert.strictEqual(response.status, 200, `expected status 200, got ${response.status}`);
    });

    // Summary
    console.log(`\n--- Results: ${passed} passed, ${failed} failed ---\n`);

    if (failed > 0) {
        process.exit(1);
    }
})();
