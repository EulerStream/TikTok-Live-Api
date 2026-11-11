import assert from "node:assert";
import * as fs from "node:fs";
import { fileURLToPath } from "node:url";

// tiktok-live-api-sdk ships the TikTok LIVE groups plus the account groups a
// LIVE integration needs. Everything else lives only in tiktok-api-sdk. The
// split is decided by spec/packages.json; these lists pin the outcome so a
// change to the rules that moves a group in or out fails here.
const REQUIRED = [
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

for (const name of REQUIRED) {
    assert.ok(classNames.includes(name), `tiktok-live-api-sdk should expose ${name}`);
}

for (const name of GENERAL_ONLY) {
    assert.ok(!classNames.includes(name), `tiktok-live-api-sdk must not expose ${name}`);
}

assert.strictEqual(
    classNames.length,
    13,
    `tiktok-live-api-sdk should expose 13 API groups, got ${classNames.length}: ${classNames.join(", ")}`,
);

console.log(`surface OK: ${classNames.length} API groups`);
