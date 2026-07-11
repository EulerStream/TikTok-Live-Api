# TikTok LIVE API (Unofficial) — Real-Time Chat, Gifts, Likes & Events

**The #1 TikTok LIVE API worldwide.** Connect to any TikTok LIVE stream and receive **real-time chat messages, gifts, likes, follows, shares, viewer counts, room stats, and PK battles** over a single managed WebSocket — with official SDKs for **Node.js / TypeScript, Python, C#, Java, and Go**. Powered by [EulerStream](https://www.eulerstream.com), the managed backend behind the popular [`TikTokLive`](https://github.com/isaackogan/TikTokLive) library.

[![Stars](https://img.shields.io/github/stars/EulerStream/EulerApiSdk?style=flat&color=0274b5)](https://github.com/EulerStream/EulerApiSdk)
[![Issues](https://img.shields.io/github/issues/EulerStream/EulerApiSdk)](https://github.com/EulerStream/EulerApiSdk/issues)
[![Patrons](https://www.eulerstream.com/api/pips/patrons?v=002)](https://www.eulerstream.com/)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

> **Updated for 2026.** Managed connections that don't break when TikTok changes — no protobuf, no reverse engineering, no maintenance on your side.

---

## Contents

- [Why EulerStream](#why-eulerstream)
- [SDKs & Supported Languages](#sdks--supported-languages)
- [Quick Start](#quick-start)
- [TikTok LIVE Events](#tiktok-live-events)
- [Common Use Cases](#common-use-cases)
- [CI / Release Pipeline](#ci--release-pipeline)
- [FAQ](#faq)
- [Enterprise](#enterprise)
- [Community](#community)
- [License](#license)

---

## Why EulerStream

TikTok does **not** publish an official public API for reading LIVE stream interaction data (chat, gifts, likes) in real time. EulerStream is the reliable, managed way to get that data — used in production by developers building **live overlays, stream alerts, TikTok LIVE games, chatbots, and analytics dashboards**.

| | EulerStream | Self-hosted / reverse-engineered libraries |
|---|:---:|:---:|
| Real-time chat, gifts, likes, follows, viewers, PK battles | ✅ | ✅ |
| Managed WebSocket (your IP never touches TikTok) | ✅ | ❌ |
| Keeps working when TikTok updates | ✅ | ⚠️ needs manual upkeep |
| Official SDKs in 5 languages | ✅ | varies |
| JWT auth, LIVE alerts, increased access limits | ✅ | ❌ |
| Free community tier | ✅ | ✅ |

> [!TIP]
> Full API documentation and the interactive OpenAPI spec are at [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi).

---

## SDKs & Supported Languages

The TikTok LIVE API is available in every major language:

| Language | Package | Install |
|----------|---------|---------|
| TypeScript / Node.js | [`@eulerstream/euler-api-sdk`](https://www.npmjs.com/package/@eulerstream/euler-api-sdk) | `npm i @eulerstream/euler-api-sdk` |
| Python | [`EulerApiSdk`](https://pypi.org/project/EulerApiSdk/) | `pip install EulerApiSdk` |
| C# / .NET | [`EulerApiSdk`](https://www.nuget.org/packages/EulerApiSdk) | `dotnet add package EulerApiSdk` |
| Java | [`io.github.isaackogan:euler-api-sdk`](https://central.sonatype.com/artifact/io.github.isaackogan/euler-api-sdk) | Maven / Gradle |
| Go | [`github.com/EulerStream/TikTok-Live-Api/sdk/go`](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go) | `go get github.com/EulerStream/TikTok-Live-Api/sdk/go` |

---

## Quick Start

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

> [!NOTE]
> Full per-language SDK docs:
> [TypeScript](./typescript-sdk/README.md) · [Python](./python-sdk/README.md) · [C#](./csharp-sdk/) · [Java](./java-sdk/) · [Go](./sdk/go/)

---

## TikTok LIVE Events

Read every real-time event from a TikTok LIVE stream using only the creator's `@username`:

- **Chat messages** — live comments from viewers
- **Gifts** — gift name, diamond count, combo/streak data
- **Likes** — like events and running like totals
- **Follows** — new followers during the stream
- **Shares** — stream share events
- **Member / join** — viewers entering the room
- **Viewer count** — live and peak viewer counts, room user stats
- **Subscribe** — new subscriptions
- **PK battles** — versus battles, scores, and results
- **Room / stream state** — LIVE start, LIVE end, and room info

---

## Common Use Cases

- **Live stream overlays** — display chat, gifts, and top gifters on screen (OBS, browser sources)
- **Gift & follow alerts** — trigger sounds, animations, or webhooks on events
- **TikTok LIVE games** — build interactive, chat-controlled or gift-controlled live games
- **Chatbots & moderation** — respond to commands and moderate chat in real time
- **Analytics** — track gifts, diamonds, viewer retention, and top supporters

---

## CI / Release Pipeline

SDKs are auto-generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi) via GitHub Actions.

| Workflow | Purpose |
|----------|---------|
| **Dry Run** | Generate & build SDKs without publishing (validation only) |
| **Release** | Generate, version, and publish to npm / PyPI / NuGet / Maven Central / Go tags |

> [!IMPORTANT]
> Releases are triggered manually via the GitHub Actions **"Run workflow"** button — no automatic publishing on push.

---

## FAQ

**Does TikTok have an official LIVE API for chat and gifts?**
No. TikTok does not offer an official public API for reading LIVE stream interaction data (chats, gifts, likes) in real time. EulerStream provides a reliable managed API that connects to TikTok's LIVE (webcast) service so you can receive these events over a WebSocket.

**How do I read TikTok LIVE chat and gifts in real time?**
Install an SDK above, add your API key, and subscribe to events for any streamer by their `@username`. You receive chat, gifts, likes, follows, viewers, and PK battle events as they happen.

**Which languages are supported?**
Node.js / TypeScript, Python, C#, Java, and Go — with a language-agnostic WebSocket for everything else.

**Is there a free tier?**
Yes. A free community tier is available; higher rate limits, more concurrent connections, LIVE alerts, JWT auth, and increased access are available on paid plans.

**Is this affiliated with TikTok?**
No. This is an independent, unofficial third-party project and is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

---

## Enterprise

<table>
<tr>
    <td><br/><img width="180px" alt="EulerStream — TikTok LIVE API" src="https://raw.githubusercontent.com/isaackogan/TikTokLive/master/.github/SquareLogo.png"><br/><br/></td>
    <td>
        <a href="https://www.eulerstream.com">
            <strong>EulerStream</strong> — managed TikTok LIVE WebSocket connections, increased access, LIVE alerts, JWT auth, and more.
        </a>
    </td>
</tr>
</table>

---

## Community

Questions, issues, or feedback? Join the [EulerStream Discord](https://www.eulerstream.com/discord).

## License

[MIT](./LICENSE)
