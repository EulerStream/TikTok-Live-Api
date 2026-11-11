import assert from "node:assert";
// Imported from the build output on purpose: this checks the names and types
// that package consumers actually receive. Run `pnpm run build` first.
import Default, { TikTokLiveApiSdk, EulerStreamApiClient } from "../dist/index.js";

assert.strictEqual(Default, TikTokLiveApiSdk, "default export should be TikTokLiveApiSdk");
assert.strictEqual(
    EulerStreamApiClient,
    TikTokLiveApiSdk,
    "deprecated EulerStreamApiClient should be the same class",
);
assert.strictEqual(TikTokLiveApiSdk.name, "TikTokLiveApiSdk");

// The deprecated name must keep working as a type as well as a value; tsc
// checks this file against dist/index.d.ts (see tsconfig.test.json).
const legacy: EulerStreamApiClient = new EulerStreamApiClient();
const current: TikTokLiveApiSdk = legacy;
assert.ok(current.rooms, "client should expose the rooms API group");

console.log("aliases OK");
