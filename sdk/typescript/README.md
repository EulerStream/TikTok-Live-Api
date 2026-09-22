# TikTok LIVE API SDK for Node.js & TypeScript

[![npm version](https://img.shields.io/npm/v/tiktok-live-api-sdk?color=0274b5)](https://www.npmjs.com/package/tiktok-live-api-sdk)
[![npm downloads](https://img.shields.io/npm/dm/tiktok-live-api-sdk)](https://www.npmjs.com/package/tiktok-live-api-sdk)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

`tiktok-live-api-sdk` is the official Node.js / TypeScript client for the [EulerStream TikTok LIVE API](https://www.eulerstream.com). Connect to any TikTok LIVE stream by `@username` and receive real-time **chat messages, gifts, likes, follows, shares, viewer counts, room stats and PK battles** over a managed WebSocket, plus fully typed clients for webcast signing, LIVE rooms, gifts, rankings, LIVE alerts, moderation, captchas and analytics.

EulerStream is the managed TikTok LIVE backend behind [TikTokLive](https://github.com/isaackogan/TikTokLive) (Python) and [TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) (Node.js). The connection layer is hosted and maintained for you, so your integration keeps working when TikTok changes its webcast protocol.

> Unofficial: this project is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

## Installation

```bash
npm install tiktok-live-api-sdk
# or
pnpm add tiktok-live-api-sdk
# or
yarn add tiktok-live-api-sdk
```

Requires Node.js 18+. Ships ESM with bundled TypeScript declarations.

> Migrating from `@eulerstream/euler-api-sdk`? That package is deprecated. Only the name changed: `npm uninstall @eulerstream/euler-api-sdk && npm install tiktok-live-api-sdk`, then update your imports.

## Quick start

1. [Create a free EulerStream account](https://www.eulerstream.com/register) (no credit card required)
2. Copy your API key from the dashboard
3. Make your first calls:

```ts
import EulerStreamApiClient from "tiktok-live-api-sdk";

const client = new EulerStreamApiClient({ apiKey: "YOUR_API_KEY" });

// Look up any TikTok user by @username
const user = await client.tikTokUsers.retrieveTikTokUserBasic("tv_asahi_news");
console.log(user.data.user?.nickname);

// Browse the TikTok LIVE gift catalog (names, diamond values, images)
const catalog = await client.gifts.listWebcastGifts();
for (const gift of catalog.data.gifts ?? []) {
  console.log(`${gift.giftName} = ${gift.diamondCount} diamonds`);
}

// Fetch the TikTok LIVE WebSocket URL + first payload for a LIVE room (protobuf)
const webcast = await client.rooms.fetchWebcastURL("7318296342189919018");
console.log(webcast.status);

// Business plan: resolve the LIVE room straight from the creator's @username
const byUsername = await client.anchors.fetchWebcastURLByUniqueId("tv_asahi_news");
```

Every method returns an Axios response (`res.status`, `res.data`, `res.headers`). The client defaults to `https://api.eulerstream.com`; pass `basePath` to override it.

## What you can build

- **Live stream overlays** for OBS and browser sources showing TikTok LIVE chat, gifts and top gifters
- **Gift and follow alerts** that trigger sounds, animations or webhooks in real time
- **TikTok LIVE games** controlled by chat commands or gifts
- **Chatbots and moderation tools** that respond to and moderate TikTok LIVE chat
- **Analytics dashboards** tracking diamonds, viewer retention and top supporters
- **LIVE monitoring**: bulk "is this creator live?" checks and LIVE start/end alerts for thousands of accounts

## API coverage

The client exposes one typed property per API group. Each is generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi), so it always matches the live API.

| Property | TikTok LIVE API group |
|---|---|
| `client.webcast` | Core TikTok LIVE: bulk live checks, webcast feed, hashtag lists, rankings |
| `client.anchors` | Creators: webcast URL by `@username`, room info / ID / cover, gift gallery, earnings, moderators, LIVE analytics |
| `client.rooms` | LIVE rooms: webcast URL by room ID, room info, room gifts, send chat |
| `client.tikTokLiveEvents` | TikTok LIVE event history for a creator |
| `client.gifts` | TikTok LIVE gift catalog: list, search and look up gifts |
| `client.rankings` | Creator leaderboards, rankings and ranking history |
| `client.agencies` | TikTok LIVE agency catalog |
| `client.alerts` / `client.alertTargets` | TikTok LIVE start/end alerts and webhook targets |
| `client.moderation` | Kicks, bans, mutes, sensitive words and comment toggles |
| `client.signing` | TikTok request signing and payload decryption |
| `client.captchas` | TikTok captcha solving |
| `client.general` | TikTok OAuth: token exchange, introspection, revocation, user info |
| `client.tikTokUsers` / `client.tikTokVideos` | TikTok user profiles and videos |
| `client.tikTokWebSocketAPI` | Your cloud WebSocket connections and their state |
| `client.accounts` / `client.authentication` / `client.analytics` | Your EulerStream account, API keys, JWTs and usage analytics |

Per-endpoint TypeScript examples for every operation are in the [EulerStream API docs](https://www.eulerstream.com/docs/intro).

## Other languages

The TikTok LIVE API SDK is also available for [Python](https://pypi.org/project/EulerApiSdk/), [C# / .NET](https://www.nuget.org/packages/EulerApiSdk), [Java](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk) and [Go](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go), and anything else can use the language-agnostic WebSocket directly.

## Links

- Website: [eulerstream.com](https://www.eulerstream.com)
- Documentation: [eulerstream.com/docs](https://www.eulerstream.com/docs/intro)
- OpenAPI reference: [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi)
- Pricing (free tier available): [eulerstream.com/pricing](https://www.eulerstream.com/pricing)
- Community: [Discord](https://www.eulerstream.com/discord)
- Source and issues: [github.com/EulerStream/TikTok-Live-Api](https://github.com/EulerStream/TikTok-Live-Api)

## License

[MIT](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE) © EulerStream
