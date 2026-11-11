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
    "TikTokSigningApi",
    "TikTokCaptchasApi",
    "TikTokUsersApi",
    "TikTokVideosApi",
];

// The OAuth group follows its tag: TikTokGeneralApi (client.general) while the
// committed spec says "TikTok General", TikTokOAuthApi (client.tikTokOAuth)
// once it carries the server's "TikTok OAuth".
const OAUTH_GROUP: Record<string, string> = {
    TikTokOAuthApi: "tikTokOAuth",
    TikTokGeneralApi: "general",
};

const manifestPath = fileURLToPath(new URL("./sdk-manifest.json", import.meta.url));
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
const apis: { className: string; propName: string }[] = manifest.apis;
const classNames: string[] = apis.map((api) => api.className);

for (const name of [...SHARED_WITH_LIVE, ...GENERAL_ONLY]) {
    assert.ok(classNames.includes(name), `tiktok-api-sdk should expose ${name}`);
}

const oauth = apis.filter((api) => api.className in OAUTH_GROUP);

assert.strictEqual(oauth.length, 1, "tiktok-api-sdk should expose the TikTok OAuth group exactly once");
assert.strictEqual(oauth[0].propName, OAUTH_GROUP[oauth[0].className], `${oauth[0].className} should be client.${OAUTH_GROUP[oauth[0].className]}`);

console.log(`surface OK: ${classNames.length} API groups`);
