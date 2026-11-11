import assert from "node:assert";
import * as fs from "node:fs";
import { fileURLToPath } from "node:url";

// tiktok-api-sdk ships every API group: the TikTok LIVE and account groups
// that tiktok-live-api-sdk also has, plus the groups that exist only here.
// No total is asserted, so the spec can add groups without touching this test.
const SHARED_WITH_LIVE = [
    "TikTokLIVEApi",
    "TikTokLIVEGiftsApi",
    "TikTokLIVEModerationApi",
    "TikTokWebSocketAPIApi",
    "AccountsApi",
    "AuthenticationApi",
];

const GENERAL_ONLY = [
    "AnalyticsApi",
    "TikTokGeneralApi",
    "TikTokSigningApi",
    "TikTokCaptchasApi",
    "TikTokUsersApi",
    "TikTokVideosApi",
];

const manifestPath = fileURLToPath(new URL("./sdk-manifest.json", import.meta.url));
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
const classNames: string[] = manifest.apis.map((api: { className: string }) => api.className);

for (const name of [...SHARED_WITH_LIVE, ...GENERAL_ONLY]) {
    assert.ok(classNames.includes(name), `tiktok-api-sdk should expose ${name}`);
}

console.log(`surface OK: ${classNames.length} API groups`);
