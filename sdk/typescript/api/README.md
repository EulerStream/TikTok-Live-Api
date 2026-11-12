# TikTok API SDK for Node.js & TypeScript

[![npm version](https://img.shields.io/npm/v/tiktok-api-sdk?color=0274b5)](https://www.npmjs.com/package/tiktok-api-sdk)
[![npm downloads](https://img.shields.io/npm/dm/tiktok-api-sdk)](https://www.npmjs.com/package/tiktok-api-sdk)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/EulerStream/TikTok-Api-Sdk/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

`tiktok-api-sdk` is the official Node.js / TypeScript client for the [EulerStream TikTok API](https://www.eulerstream.com). Use one typed TikTok API client to **look up TikTok users, videos, comments, sounds and hashtags**, **search TikTok**, run **TikTok OAuth**, **sign TikTok web requests** and **solve TikTok captchas**. The complete TikTok LIVE API is included as well, so the same client can read real-time LIVE chat, gifts and viewer counts.

The TikTok API behind this SDK is hosted by EulerStream, the managed TikTok backend behind [TikTokLive](https://github.com/isaackogan/TikTokLive) (Python) and [TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) (Node.js). Request signing, captcha solving and the LIVE connection layer are maintained for you, so your integration keeps working when TikTok changes.

> Unofficial: this project is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

Only need TikTok LIVE? [`tiktok-live-api-sdk`](https://www.npmjs.com/package/tiktok-live-api-sdk) is the same client with just the LIVE groups.

## Installation

```bash
npm install tiktok-api-sdk
# or
pnpm add tiktok-api-sdk
# or
yarn add tiktok-api-sdk
```

Requires Node.js 18+. Ships ESM with bundled TypeScript declarations.

## TikTok API quick start

1. [Create a free EulerStream account](https://www.eulerstream.com/register) (no credit card required)
2. Copy your API key from the dashboard
3. Make your first TikTok API calls:

```ts
import TikTokApiSdk from "tiktok-api-sdk";

const client = new TikTokApiSdk({ apiKey: "YOUR_API_KEY" });

// TikTok users API: look up any TikTok user by @username
const user = await client.tikTokUsers.retrieveTikTokUserBasic("tv_asahi_news");
console.log(user.data.user?.nickname);

// TikTok videos API: a creator's latest videos, newest first
const videos = await client.tikTokUsers.retrieveTikTokUserVideos("tv_asahi_news");
console.log(videos.data.videos?.length);

// TikTok LIVE API (included): list the hashtags LIVE streams are grouped under
const hashtags = await client.webcast.retrieveHashtagList();
console.log(hashtags.data.message);
```

Every method returns an Axios response (`res.status`, `res.data`, `res.headers`). The client defaults to `https://api.eulerstream.com`; pass `basePath` to override it.

## What the TikTok API covers

The client exposes one typed property per API group. Each is generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi), so it always matches the live TikTok API.

| TikTok API | Property | Methods |
|---|---|---|
| **TikTok users API** | `client.tikTokUsers` | `retrieveTikTokUserBasic`, `retrieveTikTokUserProfile`, `retrieveTikTokUserVideos`, `retrieveTikTokUserReposts`, `retrieveTikTokUserStories`, `retrieveTikTokUserPlaylists`, `retrieveTikTokPlaylistVideos`, `retrieveTikTokUserInfo`, plus the users catalog (`searchTikTokUsersCatalog`, `retrieveTikTokUsersCatalogUsername`, `retrieveTikTokUsersCatalogNumericId`) |
| **TikTok videos API** | `client.tikTokVideos` | `retrieveTikTokVideoDetailed`, `retrieveTikTokVideoComments`, `retrieveTikTokVideoCommentReplies`, `retrieveTikTokVideoCaptions`, `retrieveTikTokVideoThumbnail` |
| **TikTok search API** | `client.tikTokSearch` | `searchTikTokGeneral`, `searchTikTokVideos`, `searchTikTokUsers`, `searchTikTokPhotos`, `searchTikTokAutocomplete` |
| **TikTok sounds API** | `client.tikTokSounds` | `retrieveTikTokSound`, `retrieveTikTokSoundVideos` |
| **TikTok hashtags API** | `client.tikTokTags` | `retrieveTikTokTagVideos` |
| **TikTok short links** | `client.tikTokLinks` | `resolveTikTokShortLink` |
| **TikTok OAuth** | `client.tikTokOAuth` | `exchangeToken`, `introspectToken`, `revokeToken`, `validateRefreshToken`, `getUserInfo`, `getPublicClient` |
| **TikTok request signing** | `client.signing` | `signTikTokUrl`, plus decryptors for TikTok's encrypted payloads |
| **TikTok captcha solving** | `client.captchas` | `completePuzzleCaptcha`, `completeShapesCaptcha`, `completeIconCaptcha`, `completeWhirlCaptcha` |
| **Your account** | `client.accounts` / `client.authentication` / `client.analytics` | Account details, rate limits, API keys, JWTs and usage analytics |

Per-endpoint TypeScript examples for every TikTok API operation are in the [EulerStream API docs](https://www.eulerstream.com/docs/intro).

## TikTok LIVE API included

Everything in [`tiktok-live-api-sdk`](https://www.npmjs.com/package/tiktok-live-api-sdk) is part of this package too:

| Property | TikTok LIVE API group |
|---|---|
| `client.webcast` | Core TikTok LIVE: bulk live checks, webcast feed, hashtag lists, rankings |
| `client.anchors` | LIVE creators: webcast URL by `@username`, room info / ID / cover, gift gallery, earnings, moderators, LIVE analytics |
| `client.rooms` | LIVE rooms: webcast URL by room ID, room info, room gifts, send chat |
| `client.tikTokLiveEvents` | TikTok LIVE event history for a creator |
| `client.gifts` | TikTok LIVE gifts: the gift list, the gift catalog, search and single-gift lookup |
| `client.rankings` | LIVE creator leaderboards, rankings and ranking history |
| `client.agencies` | TikTok LIVE agency catalog |
| `client.alerts` / `client.alertTargets` | TikTok LIVE start/end alerts and webhook targets |
| `client.moderation` | LIVE kicks, bans, mutes, sensitive words and comment toggles |
| `client.tikTokWebSocketAPI` | Your cloud WebSocket connections and their state |

## What you can build with the TikTok API

- **Creator lookups and profile tools** backed by TikTok user profiles, a creator's videos, reposts, stories and playlists, and the users catalog
- **Video tools** that fetch TikTok video details, comments, replies, captions and thumbnails by ID
- **Search and discovery** across TikTok videos, users and photos, plus the videos under a hashtag or a sound
- **"Sign in with TikTok" flows** using the OAuth token, introspection and revocation routes
- **Scrapers and data pipelines** that sign TikTok web requests through the API instead of maintaining signature code
- **Captcha handling** for your own TikTok automation: puzzle, shapes, icon and whirl solvers
- **Everything TikTok LIVE**: stream overlays, gift alerts, chat bots, moderation tools and LIVE monitoring

## Migrating

Coming from `tiktok-live-api-sdk` 0.8 or earlier, or from `@eulerstream/euler-api-sdk`? This package is the same client with everything it had, so migrating is a package name change:

```bash
npm uninstall tiktok-live-api-sdk
npm install tiktok-api-sdk
```

Then point your imports at `tiktok-api-sdk`. The client class is now called `TikTokApiSdk`. The old name, `EulerStreamApiClient`, is still exported and still works, but it is deprecated and will be removed in a future major version. Default imports are unaffected, whatever you named them.
## Other languages

The TikTok API SDK is also available for [Python](https://pypi.org/project/TikTokApiSdk/), [C# / .NET](https://www.nuget.org/packages/EulerApiSdk), [Java](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk) and [Go](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go), and anything else can call the TikTok API over plain HTTP.

## Links

- Website: [eulerstream.com](https://www.eulerstream.com)
- TikTok API documentation: [eulerstream.com/docs](https://www.eulerstream.com/docs/intro)
- OpenAPI reference: [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi)
- Pricing (free tier available): [eulerstream.com/pricing](https://www.eulerstream.com/pricing)
- Community: [Discord](https://www.eulerstream.com/discord)
- Source and issues: [github.com/EulerStream/TikTok-Api-Sdk](https://github.com/EulerStream/TikTok-Api-Sdk)

## License

[MIT](https://github.com/EulerStream/TikTok-Api-Sdk/blob/master/LICENSE) © EulerStream
