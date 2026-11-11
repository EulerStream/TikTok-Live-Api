import assert from "node:assert";
// Imported from the build output on purpose: this checks the names and types
// that package consumers actually receive. Run `pnpm run build` first.
import Default, { TikTokApiSdk, EulerStreamApiClient } from "../dist/index.js";

assert.strictEqual(Default, TikTokApiSdk, "default export should be TikTokApiSdk");
assert.strictEqual(
    EulerStreamApiClient,
    TikTokApiSdk,
    "deprecated EulerStreamApiClient should be the same class",
);
assert.strictEqual(TikTokApiSdk.name, "TikTokApiSdk");

// The deprecated name must keep working as a type as well as a value; tsc
// checks this file against dist/index.d.ts (see tsconfig.test.json).
const legacy: EulerStreamApiClient = new EulerStreamApiClient();
const current: TikTokApiSdk = legacy;
assert.ok(current.tikTokUsers, "client should expose the tikTokUsers API group");

console.log("aliases OK");
