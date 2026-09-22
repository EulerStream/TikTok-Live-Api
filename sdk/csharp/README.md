# TikTok LIVE API SDK for C# / .NET

[![NuGet version](https://img.shields.io/nuget/v/EulerApiSdk?color=0274b5)](https://www.nuget.org/packages/EulerApiSdk)
[![NuGet downloads](https://img.shields.io/nuget/dt/EulerApiSdk)](https://www.nuget.org/packages/EulerApiSdk)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

`EulerApiSdk` is the official C# / .NET client for the [EulerStream TikTok LIVE API](https://www.eulerstream.com). Connect to any TikTok LIVE stream by `@username` and receive real-time **chat messages, gifts, likes, follows, shares, viewer counts, room stats and PK battles** over a managed WebSocket, plus fully typed async clients for webcast signing, LIVE rooms, gifts, rankings, LIVE alerts, moderation, captchas and analytics.

EulerStream is the managed TikTok LIVE backend behind [TikTokLiveSharp](https://github.com/frankvHoof93/TikTokLiveSharp) (C# / Unity), [TikTokLive](https://github.com/isaackogan/TikTokLive) (Python) and [TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) (Node.js). The connection layer is hosted and maintained for you, so your integration keeps working when TikTok changes its webcast protocol.

> Unofficial: this project is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

## Installation

```bash
dotnet add package EulerApiSdk
```

Or in the Package Manager console: `Install-Package EulerApiSdk`. Targets .NET 8.0 with nullable reference types enabled.

## Quick start

1. [Create a free EulerStream account](https://www.eulerstream.com/register) (no credit card required)
2. Copy your API key from the dashboard
3. Make your first calls:

```csharp
using EulerApiSdk;
using EulerApiSdk.Client;

using var client = new EulerStreamApiClient(host => host.AddTokens(new[]
{
    // Your key goes in the x-api-key header.
    new ApiKeyToken("YOUR_API_KEY", ClientUtils.ApiKeyHeader.X_api_key, prefix: ""),
    // The generated client also resolves tokens for the query-string and JWT
    // auth schemes on every call; empty placeholders satisfy it and the API ignores them.
    new ApiKeyToken("", ClientUtils.ApiKeyHeader.ApiKey, prefix: ""),
    new ApiKeyToken("", ClientUtils.ApiKeyHeader.X_jwt_key, prefix: ""),
}));

// Look up any TikTok user by @username
var user = await client.TikTokUsers.RetrieveTikTokUserBasicAsync("tv_asahi_news");
Console.WriteLine(user.Ok()?.User?.Nickname);

// Browse the TikTok LIVE gift catalog (names, diamond values, images)
var catalog = await client.TikTokLiveGifts.ListWebcastGiftsAsync();
foreach (var gift in catalog.Ok()?.Gifts ?? [])
{
    Console.WriteLine($"{gift.GiftName} = {gift.DiamondCount} diamonds");
}

// Business plan: fetch the TikTok LIVE WebSocket URL straight from the creator's @username
var webcast = await client.TikTokLiveAnchors.FetchWebcastURLByUniqueIdAsync("tv_asahi_news");
```

`EulerStreamApiClient` wires the generated API classes up with `Microsoft.Extensions.DependencyInjection` and `IHttpClientFactory`. Pass `baseAddress:` to point it at another server, and use the `configure` callback to customise HTTP clients, retry policies (Polly) or logging. Every response exposes `IsOk` / `Ok()` plus typed accessors for the documented error statuses.

## What you can build

- **Live stream overlays** for OBS and browser sources showing TikTok LIVE chat, gifts and top gifters
- **Gift and follow alerts** that trigger sounds, animations or webhooks in real time
- **TikTok LIVE games** in Unity or Godot, controlled by chat commands or gifts
- **Chatbots and moderation tools** that respond to and moderate TikTok LIVE chat
- **Analytics dashboards** tracking diamonds, viewer retention and top supporters
- **LIVE monitoring**: bulk "is this creator live?" checks and LIVE start/end alerts for thousands of accounts

## API coverage

The client exposes one typed property per API group. Each is generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi), so it always matches the live API.

| Property | TikTok LIVE API group |
|---|---|
| `client.Webcast` | Core TikTok LIVE: bulk live checks, webcast feed, hashtag lists, rankings |
| `client.TikTokLiveAnchors` | Creators: webcast URL by `@username`, room info / ID / cover, gift gallery, earnings, moderators, LIVE analytics |
| `client.TikTokLiveRooms` | LIVE rooms: webcast URL by room ID, room info, room gifts, send chat |
| `client.TikTokLiveEvents` | TikTok LIVE event history for a creator |
| `client.TikTokLiveGifts` | TikTok LIVE gift catalog: list, search and look up gifts |
| `client.TikTokLiveRankings` | Creator leaderboards, rankings and ranking history |
| `client.TikTokLiveAgencies` | TikTok LIVE agency catalog |
| `client.Alerts` / `client.AlertTargets` | TikTok LIVE start/end alerts and webhook targets |
| `client.Moderation` | Kicks, bans, mutes, sensitive words and comment toggles |
| `client.TikTokSigning` | TikTok request signing and payload decryption |
| `client.Captchas` | TikTok captcha solving |
| `client.General` | TikTok OAuth: token exchange, introspection, revocation, user info |
| `client.TikTokUsers` / `client.TikTokVideos` | TikTok user profiles and videos |
| `client.TikTokWebSocketAPI` | Your cloud WebSocket connections and their state |
| `client.Accounts` / `client.Authentication` / `client.Analytics` | Your EulerStream account, API keys, JWTs and usage analytics |

Per-endpoint C# examples for every operation are in the [EulerStream API docs](https://www.eulerstream.com/docs/intro).

## Other languages

The TikTok LIVE API SDK is also available for [Node.js / TypeScript](https://www.npmjs.com/package/tiktok-live-api-sdk), [Python](https://pypi.org/project/EulerApiSdk/), [Java](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk) and [Go](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go), and anything else can use the language-agnostic WebSocket directly.

## Links

- Website: [eulerstream.com](https://www.eulerstream.com)
- Documentation: [eulerstream.com/docs](https://www.eulerstream.com/docs/intro)
- OpenAPI reference: [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi)
- Pricing (free tier available): [eulerstream.com/pricing](https://www.eulerstream.com/pricing)
- Community: [Discord](https://www.eulerstream.com/discord)
- Source and issues: [github.com/EulerStream/TikTok-Live-Api](https://github.com/EulerStream/TikTok-Live-Api)

## License

[MIT](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE) © EulerStream
