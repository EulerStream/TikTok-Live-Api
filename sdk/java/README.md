# TikTok LIVE API SDK for Java

[![Maven Central](https://img.shields.io/maven-central/v/com.eulerstream/euler-api-sdk?color=0274b5)](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

`com.eulerstream:euler-api-sdk` is the official Java client for the [EulerStream TikTok LIVE API](https://www.eulerstream.com). Connect to any TikTok LIVE stream by `@username` and receive real-time **chat messages, gifts, likes, follows, shares, viewer counts, room stats and PK battles** over a managed WebSocket, plus a fully typed client for webcast signing, LIVE rooms, gifts, rankings, LIVE alerts, moderation, captchas and analytics.

EulerStream is the managed TikTok LIVE backend behind [TikTokLiveJava](https://github.com/jwdeveloper/TikTokLiveJava), [TikTokLive](https://github.com/isaackogan/TikTokLive) (Python) and [TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) (Node.js). The connection layer is hosted and maintained for you, so your integration keeps working when TikTok changes its webcast protocol.

> Unofficial: this project is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

## Installation

Maven:

```xml
<dependency>
    <groupId>com.eulerstream</groupId>
    <artifactId>euler-api-sdk</artifactId>
    <version>0.4.1</version>
</dependency>
```

Gradle:

```groovy
implementation 'com.eulerstream:euler-api-sdk:0.4.1'
```

Requires Java 8+. Check [Maven Central](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk) for the latest version.

## Quick start

1. [Create a free EulerStream account](https://www.eulerstream.com/register) (no credit card required)
2. Copy your API key from the dashboard
3. Make your first calls:

```java
import com.eulerstream.EulerStreamApiClient;
import com.eulerstream.model.RetrieveTikTokUserBasicResponse;
import com.eulerstream.model.TikTokGiftsServerGift;
import com.eulerstream.model.WebcastGiftcatalogResponse;

EulerStreamApiClient client = EulerStreamApiClient.builder()
    .apiKey("YOUR_API_KEY")
    .build();

// Look up any TikTok user by @username
RetrieveTikTokUserBasicResponse user = client.tikTokUsers().retrieveTikTokUserBasic("tv_asahi_news", null);
System.out.println(user.getUser().getNickname());

// Browse the TikTok LIVE gift catalog (names, diamond values, images)
WebcastGiftcatalogResponse catalog = client.tikTokLiveGifts().listWebcastGifts(null, null, null, null);
for (TikTokGiftsServerGift gift : catalog.getGifts()) {
    System.out.println(gift.getGiftName() + " = " + gift.getDiamondCount() + " diamonds");
}

// Business plan: fetch the TikTok LIVE WebSocket URL straight from the creator's @username
Object webcast = client.tikTokLiveAnchors().fetchWebcastURLByUniqueId("tv_asahi_news", null, null, null, null, null, null, null);
```

Every API group is available as a method on the client (`client.webcast()`, `client.tikTokLiveGifts()`, ...); each generated method also has a `...WithHttpInfo` variant returning `ApiResponse<T>` with the status code and headers, and `client.getApiClient()` exposes the underlying OkHttp-based `ApiClient` for timeouts, proxies and interceptors.

## What you can build

- **Live stream overlays** for OBS and browser sources showing TikTok LIVE chat, gifts and top gifters
- **Gift and follow alerts** that trigger sounds, animations or webhooks in real time
- **TikTok LIVE games** and Minecraft / Spigot plugins controlled by chat commands or gifts
- **Chatbots and moderation tools** that respond to and moderate TikTok LIVE chat
- **Analytics dashboards** tracking diamonds, viewer retention and top supporters
- **LIVE monitoring**: bulk "is this creator live?" checks and LIVE start/end alerts for thousands of accounts

## API coverage

The client exposes one typed accessor per API group. Each is generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi), so it always matches the live API.

| Accessor | TikTok LIVE API group |
|---|---|
| `client.webcast()` | Core TikTok LIVE: bulk live checks, webcast feed, hashtag lists, rankings |
| `client.tikTokLiveAnchors()` | Creators: webcast URL by `@username`, room info / ID / cover, gift gallery, earnings, moderators, LIVE analytics |
| `client.tikTokLiveRooms()` | LIVE rooms: webcast URL by room ID, room info, room gifts, send chat |
| `client.tikTokLiveEvents()` | TikTok LIVE event history for a creator |
| `client.tikTokLiveGifts()` | TikTok LIVE gift catalog: list, search and look up gifts |
| `client.tikTokLiveRankings()` | Creator leaderboards, rankings and ranking history |
| `client.tikTokLiveAgencies()` | TikTok LIVE agency catalog |
| `client.alerts()` / `client.alertTargets()` | TikTok LIVE start/end alerts and webhook targets |
| `client.moderation()` | Kicks, bans, mutes, sensitive words and comment toggles |
| `client.tikTokSigning()` | TikTok request signing and payload decryption |
| `client.captchas()` | TikTok captcha solving |
| `client.general()` | TikTok OAuth: token exchange, introspection, revocation, user info |
| `client.tikTokUsers()` / `client.tikTokVideos()` | TikTok user profiles and videos |
| `client.tikTokWebSocketApi()` | Your cloud WebSocket connections and their state |
| `client.accounts()` / `client.authentication()` / `client.analytics()` | Your EulerStream account, API keys, JWTs and usage analytics |

Per-endpoint Java examples for every operation are in the [EulerStream API docs](https://www.eulerstream.com/docs/intro).

## Other languages

The TikTok LIVE API SDK is also available for [Node.js / TypeScript](https://www.npmjs.com/package/tiktok-live-api-sdk), [Python](https://pypi.org/project/EulerApiSdk/), [C# / .NET](https://www.nuget.org/packages/EulerApiSdk) and [Go](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go), and anything else can use the language-agnostic WebSocket directly.

## Links

- Website: [eulerstream.com](https://www.eulerstream.com)
- Documentation: [eulerstream.com/docs](https://www.eulerstream.com/docs/intro)
- OpenAPI reference: [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi)
- Pricing (free tier available): [eulerstream.com/pricing](https://www.eulerstream.com/pricing)
- Community: [Discord](https://www.eulerstream.com/discord)
- Source and issues: [github.com/EulerStream/TikTok-Live-Api](https://github.com/EulerStream/TikTok-Live-Api)

## License

[MIT](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE) © EulerStream
