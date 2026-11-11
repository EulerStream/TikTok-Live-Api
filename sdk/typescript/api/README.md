# TikTok API SDK for Node.js & TypeScript

[![npm version](https://img.shields.io/npm/v/tiktok-api-sdk?color=0274b5)](https://www.npmjs.com/package/tiktok-api-sdk)
[![npm downloads](https://img.shields.io/npm/dm/tiktok-api-sdk)](https://www.npmjs.com/package/tiktok-api-sdk)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

`tiktok-api-sdk` is the official Node.js / TypeScript client for the [EulerStream TikTok API](https://www.eulerstream.com). Look up **TikTok user profiles and videos**, run **TikTok OAuth**, **sign TikTok web requests** and **solve TikTok captchas** from fully typed clients. The complete TikTok LIVE API is included too: connect to any LIVE stream by `@username` and receive real-time chat messages, gifts, likes, follows, viewer counts and PK battles, with clients for LIVE rooms, gifts, rankings, alerts and moderation.

EulerStream is the managed TikTok backend behind [TikTokLive](https://github.com/isaackogan/TikTokLive) (Python) and [TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) (Node.js). Signing, captcha solving and the LIVE connection layer are hosted and maintained for you, so your integration keeps working when TikTok changes.

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

## Quick start

1. [Create a free EulerStream account](https://www.eulerstream.com/register) (no credit card required)
2. Copy your API key from the dashboard
3. Make your first calls:

```ts
import TikTokApiSdk from "tiktok-api-sdk";

const client = new TikTokApiSdk({ apiKey: "YOUR_API_KEY" });

// Look up any TikTok user by @username
const user = await client.tikTokUsers.retrieveTikTokUserBasic("tv_asahi_news");
console.log(user.data.user?.nickname);

// TikTok LIVE is included: list the hashtags LIVE streams are grouped under
const hashtags = await client.webcast.retrieveHashtagList();
console.log(hashtags.data.message);

// Get the TikTok LIVE gift list (names, diamond values, images) as a JSON file to download
const gifts = await client.gifts.retrieveWebcastGifts();
console.log(gifts.data.url);
```

Every method returns an Axios response (`res.status`, `res.data`, `res.headers`). The client defaults to `https://api.eulerstream.com`; pass `basePath` to override it.

## What you can build

- **Creator lookups and profile tools** backed by TikTok user profiles and the users catalog
- **Video tools** that fetch TikTok video details and thumbnails by ID
- **"Sign in with TikTok" flows** using the OAuth token, introspection and revocation routes
- **Scrapers and data pipelines** that sign TikTok web requests through the API instead of maintaining signature code
- **Captcha handling** for your own TikTok automation: puzzle, shapes, icon and whirl solvers
- **Everything TikTok LIVE**: stream overlays, gift alerts, chat bots, moderation tools and LIVE monitoring

## API coverage

The client exposes one typed property per API group. Each is generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi), so it always matches the live API.

| Property | TikTok API group |
|---|---|
| `client.tikTokUsers` | TikTok user profiles and the users catalog |
| `client.tikTokVideos` | TikTok video details and thumbnails |
| `client.general` | TikTok OAuth: token exchange, introspection, revocation, user info |
| `client.signing` | TikTok request signing and payload decryption |
| `client.captchas` | TikTok captcha solving |
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
| `client.accounts` / `client.authentication` / `client.analytics` | Your EulerStream account, API keys, JWTs and usage analytics |

Per-endpoint TypeScript examples for every operation are in the [EulerStream API docs](https://www.eulerstream.com/docs/intro).

## Migrating

Coming from `tiktok-live-api-sdk` 0.x or `@eulerstream/euler-api-sdk`? This package is the same client with everything it had, so migrating is a package name change:

```bash
npm uninstall tiktok-live-api-sdk
npm install tiktok-api-sdk
```

Then point your imports at `tiktok-api-sdk`. The client class is now called `TikTokApiSdk`. The old name, `EulerStreamApiClient`, is still exported and still works, but it is deprecated and will be removed in a future major version. Default imports are unaffected, whatever you named them.

## Other languages

The TikTok API SDK is also available for [Python](https://pypi.org/project/tiktok-api-sdk/), [C# / .NET](https://www.nuget.org/packages/EulerApiSdk), [Java](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk) and [Go](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go), and anything else can use the language-agnostic WebSocket directly.

## Links

- Website: [eulerstream.com](https://www.eulerstream.com)
- Documentation: [eulerstream.com/docs](https://www.eulerstream.com/docs/intro)
- OpenAPI reference: [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi)
- Pricing (free tier available): [eulerstream.com/pricing](https://www.eulerstream.com/pricing)
- Community: [Discord](https://www.eulerstream.com/discord)
- Source and issues: [github.com/EulerStream/TikTok-Live-Api](https://github.com/EulerStream/TikTok-Live-Api)

## License

[MIT](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE) © EulerStream
