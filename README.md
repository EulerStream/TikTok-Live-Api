# TikTok API & TikTok LIVE API SDK (Unofficial)

The [TikTok API](https://www.eulerstream.com/) SDK gives you typed clients for TikTok **user profiles, videos, OAuth, request signing and captcha solving**, plus the complete **TikTok LIVE API**: connect to any TikTok LIVE stream and receive real-time chat messages, gifts, likes, follows, shares, viewer counts, room stats and PK battles over a single managed WebSocket. Official SDKs for Node.js/TypeScript, Python, C#, Java and Go. Powered by [EulerStream](https://www.eulerstream.com), the managed backend behind the popular [`TikTokLive`](https://github.com/isaackogan/TikTokLive) library.

[![Stars](https://img.shields.io/github/stars/EulerStream/TikTok-Api-Sdk?style=flat&color=0274b5)](https://github.com/EulerStream/TikTok-Api-Sdk)
[![Issues](https://img.shields.io/github/issues/EulerStream/TikTok-Api-Sdk)](https://github.com/EulerStream/TikTok-Api-Sdk/issues)
[![Patrons](https://www.eulerstream.com/api/pips/patrons?v=002)](https://www.eulerstream.com/)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

> Updated for 2026. One TikTok API for data and LIVE, hosted and kept working when TikTok changes. No signature code to maintain, no protobuf parsing, no reverse engineering on your side.

---

## Contents

- [What the TikTok API Covers](#what-the-tiktok-api-covers)
- [Why EulerStream](#why-eulerstream)
- [SDKs & Supported Languages](#sdks--supported-languages)
- [Quick Start](#quick-start)
- [TikTok LIVE API Events](#tiktok-live-api-events)
- [Common Use Cases](#common-use-cases)
- [Community Libraries](#community-libraries)
- [Plans & Pricing](#plans--pricing)
- [CI / Release Pipeline](#ci--release-pipeline)
- [FAQ](#faq)
- [Enterprise](#enterprise)
- [Community](#community)
- [License](#license)

---

## What the TikTok API Covers

One API key and one client cover both sides of TikTok:

| | What you get |
|---|---|
| **TikTok users** | Public profile lookups by `@username` or ID, and a searchable users catalog |
| **TikTok videos** | Video details and thumbnails by video ID |
| **TikTok OAuth** | Token exchange, introspection, revocation and user info for "Sign in with TikTok" flows |
| **TikTok request signing** | Sign TikTok web requests and decrypt TikTok payloads through the API |
| **TikTok captchas** | Puzzle, shapes, icon and whirl captcha solvers |
| **TikTok LIVE API** | Real-time LIVE events over a WebSocket, plus LIVE rooms, creators, gifts, rankings, LIVE alerts, moderation and agencies |

Only need LIVE? The TypeScript and Python SDKs also come as a smaller [LIVE-only package](#sdks--supported-languages) with just the TikTok LIVE API.

Full API documentation and the interactive OpenAPI spec live at [eulerstream.com/docs](https://www.eulerstream.com/docs/intro).

---

## Why EulerStream

TikTok does not publish a public API for reading LIVE stream interaction data (chat, gifts, likes) in real time, and calling TikTok's web endpoints yourself means maintaining request signatures and solving captchas. EulerStream fills that gap with a managed TikTok API used in production for creator tools, data pipelines, live overlays, stream alerts, TikTok LIVE games, chatbots and analytics dashboards.

The core difference from self-hosted libraries is who carries the maintenance burden. Reverse-engineered signatures and connections break whenever TikTok updates its web or webcast protocol, and your own IP is exposed to TikTok directly. With EulerStream, signing, captcha solving and the LIVE connection layer are hosted and maintained for you.

| | EulerStream | Self-hosted / reverse-engineered |
|---|:---:|:---:|
| TikTok user and video lookups | Yes | Varies |
| TikTok request signing and captcha solving | Yes | Needs manual upkeep |
| Real-time LIVE chat, gifts, likes, follows, viewers, PK battles | Yes | Yes |
| Managed WebSocket (your IP never touches TikTok) | Yes | No |
| Keeps working when TikTok updates | Yes | Needs manual upkeep |
| Official SDKs in 5 languages | Yes | Varies |
| OAuth, JWT auth, LIVE alerts, moderation routes | Yes | No |
| Free community tier | Yes | Yes |

---

## SDKs & Supported Languages

| Language | Package | Install |
|----------|---------|---------|
| TypeScript / Node.js | [`tiktok-api-sdk`](https://www.npmjs.com/package/tiktok-api-sdk) (TikTok API + TikTok LIVE API) · [`tiktok-live-api-sdk`](https://www.npmjs.com/package/tiktok-live-api-sdk) (TikTok LIVE API only) | `npm i tiktok-api-sdk` or `npm i tiktok-live-api-sdk` |
| Python | [`TikTokApiSdk`](https://pypi.org/project/TikTokApiSdk/) (TikTok API + TikTok LIVE API) · [`TikTokLiveApiSdk`](https://pypi.org/project/TikTokLiveApiSdk/) (TikTok LIVE API only) | `pip install TikTokApiSdk` or `pip install TikTokLiveApiSdk` |
| C# / .NET | [`EulerApiSdk`](https://www.nuget.org/packages/EulerApiSdk) | `dotnet add package EulerApiSdk` |
| Java | [`com.eulerstream:euler-api-sdk`](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk) | Maven / Gradle |
| Go | [`github.com/EulerStream/TikTok-Live-Api/sdk/go`](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go) | `go get github.com/EulerStream/TikTok-Live-Api/sdk/go` |

TypeScript and Python each come as two packages. The full one (`tiktok-api-sdk` on npm, `TikTokApiSdk` on PyPI) has everything: TikTok user profiles, videos, OAuth, request signing and captcha solving, plus the full TikTok LIVE API. The LIVE one (`tiktok-live-api-sdk` on npm, `TikTokLiveApiSdk` on PyPI) is the same client with only the TikTok LIVE routes. C#, Java and Go ship everything in one package.

Everything else can use the language-agnostic WebSocket directly. A [payload decoder tool](https://www.eulerstream.com/docs/api/client-sdks/websocket-sdk/decoder) is available for debugging.

---

## Quick Start

1. [Create a free account](https://www.eulerstream.com/register) (no credit card required)
2. Grab your API key from the dashboard
3. Install an SDK and make your first calls

### TypeScript / Node.js

```ts
import TikTokApiSdk from "tiktok-api-sdk";

const client = new TikTokApiSdk({ apiKey: "YOUR_API_KEY" });

// TikTok API: look up any TikTok user by @username
const user = await client.tikTokUsers.retrieveTikTokUserBasic("tv_asahi_news");
console.log(user.data.user?.nickname);

// TikTok LIVE API: list the hashtags LIVE streams are grouped under
const hashtags = await client.webcast.retrieveHashtagList();
console.log(hashtags.data.message);

// Business plan: fetch the TikTok LIVE WebSocket URL straight from the creator's @username
const webcast = await client.anchors.fetchWebcastURLByUniqueId("tv_asahi_news");
```

### Python

```python
from TikTokApiSdk import AuthenticatedClient
from TikTokApiSdk.api.tik_tok_users import retrieve_tik_tok_user_basic
from TikTokApiSdk.api.tik_tok_live import retrieve_hashtag_list

client = AuthenticatedClient(base_url="https://api.eulerstream.com", token="YOUR_API_KEY")

with client as c:
    # TikTok API: look up any TikTok user by @username
    user = retrieve_tik_tok_user_basic.sync(unique_id="tv_asahi_news", client=c)
    print(user.user.nickname)

    # TikTok LIVE API: list the hashtags LIVE streams are grouped under
    hashtags = retrieve_hashtag_list.sync(client=c)
    print(hashtags.message)
```

Both examples use the full package. With the LIVE-only package the LIVE calls are the same apart from the name: `TikTokLiveApiSdk` in place of `TikTokApiSdk`.

Per-language SDK docs: TypeScript ([TikTok API](./sdk/typescript/api/README.md) · [TikTok LIVE API](./sdk/typescript/live/README.md)) · Python ([TikTok API](https://pypi.org/project/TikTokApiSdk/) · [TikTok LIVE API](https://pypi.org/project/TikTokLiveApiSdk/)) · [C#](./sdk/csharp/README.md) · [Java](./sdk/java/README.md) · [Go](./sdk/go/README.md)

---

## TikTok LIVE API Events

Subscribe to every real-time event from a TikTok LIVE stream using only the creator's `@username`:

- **Chat messages**: live comments from viewers
- **Gifts**: gift name, diamond count, combo/streak data
- **Likes**: like events and running like totals
- **Follows**: new followers during the stream
- **Shares**: stream share events
- **Member / join**: viewers entering the room
- **Viewer count**: live and peak viewer counts, room user stats
- **Subscribe**: new subscriptions
- **PK battles**: versus battles, scores, and results
- **Room / stream state**: LIVE start, LIVE end, and room info

Beyond the event stream, the TikTok LIVE REST API covers the gift catalog, room covers and video URLs, bulk live checks, creator leaderboards and rankings, and moderation actions (bans, mutes, sensitive words, moderator management). The full route catalog is on the [pricing page](https://www.eulerstream.com/pricing).

---

## Common Use Cases

**With the TikTok API**

- **Creator lookups and profile tools**: resolve a `@username` to a public TikTok profile, or search the users catalog
- **Video tools**: fetch TikTok video details and thumbnails by ID
- **"Sign in with TikTok"**: run the OAuth token flow for your own app
- **Scrapers and data pipelines**: sign TikTok web requests through the API instead of maintaining signature code
- **Captcha handling**: solve TikTok puzzle, shapes, icon and whirl captchas in your own automation

**With the TikTok LIVE API**

- **Live stream overlays**: display chat, gifts, and top gifters on screen (OBS, browser sources)
- **Gift & follow alerts**: trigger sounds, animations, or webhooks on events
- **TikTok LIVE games**: build interactive, chat-controlled or gift-controlled live games
- **Chatbots & moderation**: respond to commands and moderate chat in real time
- **Analytics**: track gifts, diamonds, viewer retention, and top supporters
- **Hardware integrations**: anything you can wire up, like a [thermal printer that prints gifts live](https://www.youtube.com/watch?v=dshDn17RqMw)

---

## Community Libraries

Several popular open-source TikTok LIVE libraries integrate with EulerStream out of the box:

| Library | Language | Repo |
|---------|----------|------|
| TikTok-Live-Connector | Node.js | [zerodytrash/TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) |
| TikTokLive | Python | [isaackogan/TikTokLive](https://github.com/isaackogan/TikTokLive) |
| TikTokLiveSharp | C# / Unity | [frankvHoof93/TikTokLiveSharp](https://github.com/frankvHoof93/TikTokLiveSharp) |
| TikTokLiveJava | Java | [jwdeveloper/TikTokLiveJava](https://github.com/jwdeveloper/TikTokLiveJava) |
| TikTokLiveRust | Rust | [jwdeveloper/TikTokLiveRust](https://github.com/jwdeveloper/TikTokLiveRust) |
| gotiktoklive | Go | [steampoweredtaco/gotiktoklive](https://github.com/steampoweredtaco/gotiktoklive) |

---

## Plans & Pricing

| | Community | Business | Enterprise |
|---|---|---|---|
| Price | Free, forever | $50/month (48-hour free trial) | Custom |
| Requests / day | 2,500 | 10,000 | 250,000+ |
| Cloud WebSockets | 25 | 100 | 1,500+ |
| TikTok LIVE alerts | 5 | 50 | 1,000+ |
| TikTok image CDN | Basic | Full | Full |

Add-ons such as premium webcast routes, priority API requests, signature routes, CAPTCHA routes, and ranking catalog routes are available on paid plans. See [eulerstream.com/pricing](https://www.eulerstream.com/pricing) for current details.

---

## CI / Release Pipeline

SDKs are generated via GitHub Actions from the OpenAPI document committed at [`spec/openapi.json`](./spec/openapi.json). It is the public document the API server emits from its own source (`openapi:emit -- --public` in the `euler-api-server` app), so a release is generated from a reviewed, versioned spec rather than from whatever a running server happens to serve. Refresh it with `scripts/refresh-spec.sh <path-to-euler-api-server-app>`, which also refreshes the private SDK's full document, then commit the result.

For TypeScript and Python, the same spec produces both packages: the full one from the full document and the LIVE one from the TikTok LIVE subset declared in [`spec/packages.json`](./spec/packages.json).

| Workflow | Purpose |
|----------|---------|
| Dry Run | Generate and build SDKs without publishing (validation only) |
| Release | Generate, version, and publish to npm / PyPI / NuGet / Maven Central / Go tags |

Releases are triggered manually via the GitHub Actions "Run workflow" button. Nothing publishes automatically on push.

---

## FAQ

**What is this TikTok API?**
An unofficial, managed API for TikTok operated by EulerStream. It covers TikTok user profiles, videos, OAuth, request signing and captcha solving, and includes the TikTok LIVE API for real-time stream events. You call it with an API key through one of the SDKs above or over plain HTTP.

**Is this the official TikTok API?**
No. TikTok's own developer platform offers official APIs to approved apps. This is an independent, unofficial third-party project. It is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

**How do I look up a TikTok user or video with an API?**
Install `tiktok-api-sdk` from npm or `TikTokApiSdk` from PyPI (or the C#, Java or Go SDK), add your API key, and call the users or videos client with a `@username` or video ID, as in the Quick Start above.

**Does TikTok have an official LIVE API for chat and gifts?**
No. TikTok does not offer an official public API for reading LIVE stream interaction data (chats, gifts, likes) in real time. EulerStream's TikTok LIVE API connects to TikTok's LIVE (webcast) service so you can receive these events over a WebSocket.

**How do I read TikTok LIVE chat and gifts in real time?**
Install an SDK above, add your API key, and subscribe to events for any streamer by their `@username`. Chat, gifts, likes, follows, viewer counts, and PK battle events arrive as they happen.

**Should I install the full package or the LIVE-only one?**
The full package (`tiktok-api-sdk` on npm, `TikTokApiSdk` on PyPI) has everything, including the TikTok LIVE API. The LIVE-only one (`tiktok-live-api-sdk` on npm, `TikTokLiveApiSdk` on PyPI) is smaller, with only the LIVE routes. If you are unsure, install the full package.

**Which languages are supported?**
Node.js/TypeScript, Python, C#, Java, and Go, plus a language-agnostic WebSocket for everything else.

**Is there a free tier?**
Yes. The Community tier is free forever and includes 2,500 requests per day, 25 cloud WebSockets, and 5 LIVE alerts. Higher limits and additional routes are available on the Business ($50/month) and Enterprise plans.

---

## Enterprise

<table>
<tr>
    <td><br/><img width="180px" alt="EulerStream TikTok API and TikTok LIVE API" src="https://raw.githubusercontent.com/isaackogan/TikTokLive/master/.github/SquareLogo.png"><br/><br/></td>
    <td>
        <a href="https://www.eulerstream.com">
            <strong>EulerStream</strong>: managed TikTok API and TikTok LIVE WebSocket connections, 250,000+ requests/day, LIVE alerts, JWT auth, and dedicated support.
        </a>
        <br/><br/>
        Need custom volume or SLAs? <a href="https://www.eulerstream.com/enterprise-inquiries">Schedule a call</a>.
    </td>
</tr>
</table>

---

## Community

Questions, issues, or feedback? Join the [EulerStream Discord](https://www.eulerstream.com/discord) or open a [GitHub issue](https://github.com/EulerStream/TikTok-Api-Sdk/issues).

## License

[MIT](./LICENSE)
