# TikTok LIVE API (Unofficial): Real-Time Chat, Gifts, Likes & Events

Our [TikTok LIVE API](https://www.eulerstream.com/) allows you to connect to any TikTok LIVE stream and receive real-time chat messages, gifts, likes, follows, shares, viewer counts, room stats, and PK battles over a single managed WebSocket. Official SDKs for Node.js/TypeScript, Python, C#, Java, and Go. Powered by [EulerStream](https://www.eulerstream.com), the managed backend behind the popular [`TikTokLive`](https://github.com/isaackogan/TikTokLive) library.

[![Stars](https://img.shields.io/github/stars/EulerStream/EulerApiSdk?style=flat&color=0274b5)](https://github.com/EulerStream/EulerApiSdk)
[![Issues](https://img.shields.io/github/issues/EulerStream/EulerApiSdk)](https://github.com/EulerStream/EulerApiSdk/issues)
[![Patrons](https://www.eulerstream.com/api/pips/patrons?v=002)](https://www.eulerstream.com/)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

> Updated for 2026. Managed connections that keep working when TikTok changes. No protobuf parsing, no reverse engineering, no maintenance on your side.

---

## Contents

- [Why EulerStream](#why-eulerstream)
- [SDKs & Supported Languages](#sdks--supported-languages)
- [Quick Start](#quick-start)
- [TikTok LIVE Events](#tiktok-live-events)
- [Common Use Cases](#common-use-cases)
- [Community Libraries](#community-libraries)
- [Plans & Pricing](#plans--pricing)
- [CI / Release Pipeline](#ci--release-pipeline)
- [FAQ](#faq)
- [Enterprise](#enterprise)
- [Community](#community)
- [License](#license)

---

## Why EulerStream

TikTok does not publish an official public API for reading LIVE stream interaction data (chat, gifts, likes) in real time. EulerStream fills that gap with a managed API used in production for live overlays, stream alerts, TikTok LIVE games, chatbots, and analytics dashboards.

The core difference from self-hosted libraries is who carries the maintenance burden. Reverse-engineered connections break whenever TikTok updates its webcast protocol, and your own IP is exposed to TikTok directly. With EulerStream, the connection layer is hosted and maintained for you.

| | EulerStream | Self-hosted / reverse-engineered |
|---|:---:|:---:|
| Real-time chat, gifts, likes, follows, viewers, PK battles | Yes | Yes |
| Managed WebSocket (your IP never touches TikTok) | Yes | No |
| Keeps working when TikTok updates | Yes | Needs manual upkeep |
| Official SDKs in 5 languages | Yes | Varies |
| JWT auth, LIVE alerts, moderation routes | Yes | No |
| Free community tier | Yes | Yes |

Full API documentation and the interactive OpenAPI spec live at [eulerstream.com/docs](https://www.eulerstream.com/docs/intro).

---

## SDKs & Supported Languages

| Language | Package | Install |
|----------|---------|---------|
| TypeScript / Node.js | [`@eulerstream/euler-api-sdk`](https://www.npmjs.com/package/@eulerstream/euler-api-sdk) | `npm i @eulerstream/euler-api-sdk` |
| Python | [`EulerApiSdk`](https://pypi.org/project/EulerApiSdk/) | `pip install EulerApiSdk` |
| C# / .NET | [`EulerApiSdk`](https://www.nuget.org/packages/EulerApiSdk) | `dotnet add package EulerApiSdk` |
| Java | [`io.github.isaackogan:euler-api-sdk`](https://central.sonatype.com/artifact/io.github.isaackogan/euler-api-sdk) | Maven / Gradle |
| Go | [`github.com/EulerStream/TikTok-Live-Api/sdk/go`](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go) | `go get github.com/EulerStream/TikTok-Live-Api/sdk/go` |

Everything else can use the language-agnostic WebSocket directly. A [payload decoder tool](https://www.eulerstream.com/docs/api/client-sdks/websocket-sdk/decoder) is available for debugging.

---

## Quick Start

1. [Create a free account](https://www.eulerstream.com/register) (no credit card required)
2. Grab your API key from the dashboard
3. Install an SDK and connect

### TypeScript / Node.js

```ts
import EulerStreamApiClient from "@eulerstream/euler-api-sdk";

const client = new EulerStreamApiClient({ apiKey: "YOUR_API_KEY" });

// Fetch a TikTok LIVE webcast URL for any streamer
const res = await client.webcast.fetchWebcastURL("ttlive-node", undefined, "tv_asahi_news");
console.log(res.status, res.data);
```

### Python

```python
from EulerApiSdk import AuthenticatedClient
from EulerApiSdk.api.tik_tok_live import fetch_webcast_url

client = AuthenticatedClient(base_url="https://api.eulerstream.com", token="YOUR_API_KEY")

with client as c:
    response = fetch_webcast_url.sync_detailed(client=c)
    print(response.status_code, response.parsed)
```

Per-language SDK docs: [TypeScript](./typescript-sdk/README.md) · [Python](./python-sdk/README.md) · [C#](./csharp-sdk/) · [Java](./java-sdk/) · [Go](./sdk/go/)

---

## TikTok LIVE Events

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

Beyond the event stream, the REST API covers the gift catalog, room covers and video URLs, bulk live checks, creator leaderboards and rankings, and moderation actions (bans, mutes, sensitive words, moderator management). The full route catalog is on the [pricing page](https://www.eulerstream.com/pricing).

---

## Common Use Cases

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

SDKs are auto-generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi) via GitHub Actions.

| Workflow | Purpose |
|----------|---------|
| Dry Run | Generate and build SDKs without publishing (validation only) |
| Release | Generate, version, and publish to npm / PyPI / NuGet / Maven Central / Go tags |

Releases are triggered manually via the GitHub Actions "Run workflow" button. Nothing publishes automatically on push.

---

## FAQ

**Does TikTok have an official LIVE API for chat and gifts?**
No. TikTok does not offer an official public API for reading LIVE stream interaction data (chats, gifts, likes) in real time. EulerStream provides a managed API that connects to TikTok's LIVE (webcast) service so you can receive these events over a WebSocket.

**How do I read TikTok LIVE chat and gifts in real time?**
Install an SDK above, add your API key, and subscribe to events for any streamer by their `@username`. Chat, gifts, likes, follows, viewer counts, and PK battle events arrive as they happen.

**Which languages are supported?**
Node.js/TypeScript, Python, C#, Java, and Go, plus a language-agnostic WebSocket for everything else.

**Is there a free tier?**
Yes. The Community tier is free forever and includes 2,500 requests per day, 25 cloud WebSockets, and 5 LIVE alerts. Higher limits and additional routes are available on the Business ($50/month) and Enterprise plans.

**Is this affiliated with TikTok?**
No. This is an independent, unofficial third-party project. It is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

---

## Enterprise

<table>
<tr>
    <td><br/><img width="180px" alt="EulerStream TikTok LIVE API" src="https://raw.githubusercontent.com/isaackogan/TikTokLive/master/.github/SquareLogo.png"><br/><br/></td>
    <td>
        <a href="https://www.eulerstream.com">
            <strong>EulerStream</strong>: managed TikTok LIVE WebSocket connections, 250,000+ requests/day, LIVE alerts, JWT auth, and dedicated support.
        </a>
        <br/><br/>
        Need custom volume or SLAs? <a href="https://www.eulerstream.com/enterprise-inquiries">Schedule a call</a>.
    </td>
</tr>
</table>

---

## Community

Questions, issues, or feedback? Join the [EulerStream Discord](https://www.eulerstream.com/discord) or open a [GitHub issue](https://github.com/EulerStream/EulerApiSdk/issues).

## License

[MIT](./LICENSE)
