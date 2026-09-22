# TikTok LIVE API SDK for Go

[![Go Reference](https://pkg.go.dev/badge/github.com/EulerStream/TikTok-Live-Api/sdk/go.svg)](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2)](https://www.eulerstream.com/discord)

`github.com/EulerStream/TikTok-Live-Api/sdk/go` is the official Go client for the [EulerStream TikTok LIVE API](https://www.eulerstream.com). Connect to any TikTok LIVE stream by `@username` and receive real-time **chat messages, gifts, likes, follows, shares, viewer counts, room stats and PK battles** over a managed WebSocket, plus a fully typed client for webcast signing, LIVE rooms, gifts, rankings, LIVE alerts, moderation, captchas and analytics.

EulerStream is the managed TikTok LIVE backend behind [gotiktoklive](https://github.com/steampoweredtaco/gotiktoklive), [TikTokLive](https://github.com/isaackogan/TikTokLive) (Python) and [TikTok-Live-Connector](https://github.com/zerodytrash/TikTok-Live-Connector) (Node.js). The connection layer is hosted and maintained for you, so your integration keeps working when TikTok changes its webcast protocol.

> Unofficial: this project is not affiliated with, endorsed by, or connected to TikTok or ByteDance.

## Installation

```bash
go get github.com/EulerStream/TikTok-Live-Api/sdk/go
```

Requires Go 1.18+. The module has no dependencies outside the standard library.

## Quick start

1. [Create a free EulerStream account](https://www.eulerstream.com/register) (no credit card required)
2. Copy your API key from the dashboard
3. Make your first calls:

```go
package main

import (
	"context"
	"fmt"

	eulerstream "github.com/EulerStream/TikTok-Live-Api/sdk/go"
)

func main() {
	ctx := context.Background()
	client := eulerstream.NewEulerStreamClient(eulerstream.WithAPIKey("YOUR_API_KEY"))

	// Look up any TikTok user by @username
	user, _, err := client.TikTokUsers.RetrieveTikTokUserBasic(ctx, "tv_asahi_news").Execute()
	if err != nil {
		panic(err)
	}
	fmt.Println(user.GetUser().Nickname)

	// Browse the TikTok LIVE gift catalog (names, diamond values, images)
	catalog, _, err := client.TikTokLiveGifts.ListWebcastGifts(ctx).Execute()
	if err != nil {
		panic(err)
	}
	for _, gift := range catalog.Gifts {
		fmt.Printf("%s = %v diamonds\n", gift.GiftName, gift.DiamondCount)
	}

	// Business plan: fetch the TikTok LIVE WebSocket URL straight from the creator's @username
	webcast, _, err := client.TikTokLiveAnchors.FetchWebcastURLByUniqueId(ctx, "tv_asahi_news").Execute()
	_ = webcast
}
```

Every call returns `(result, *http.Response, error)`. Use `eulerstream.WithHTTPClient` to supply your own `*http.Client` (timeouts, proxies, transports) and `client.Raw` for the underlying generated `APIClient`.

## What you can build

- **Live stream overlays** for OBS and browser sources showing TikTok LIVE chat, gifts and top gifters
- **Gift and follow alerts** that trigger sounds, animations or webhooks in real time
- **TikTok LIVE games** controlled by chat commands or gifts
- **Chatbots and moderation tools** that respond to and moderate TikTok LIVE chat
- **Analytics dashboards** tracking diamonds, viewer retention and top supporters
- **LIVE monitoring**: bulk "is this creator live?" checks and LIVE start/end alerts for thousands of accounts

## API coverage

The client exposes one typed field per API group. Each is generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi), so it always matches the live API.

| Field | TikTok LIVE API group |
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

Per-endpoint Go examples for every operation are in the [EulerStream API docs](https://www.eulerstream.com/docs/intro).

## Other languages

The TikTok LIVE API SDK is also available for [Node.js / TypeScript](https://www.npmjs.com/package/tiktok-live-api-sdk), [Python](https://pypi.org/project/EulerApiSdk/), [C# / .NET](https://www.nuget.org/packages/EulerApiSdk) and [Java](https://central.sonatype.com/artifact/com.eulerstream/euler-api-sdk), and anything else can use the language-agnostic WebSocket directly.

## Links

- Website: [eulerstream.com](https://www.eulerstream.com)
- Documentation: [eulerstream.com/docs](https://www.eulerstream.com/docs/intro)
- OpenAPI reference: [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi)
- Pricing (free tier available): [eulerstream.com/pricing](https://www.eulerstream.com/pricing)
- Community: [Discord](https://www.eulerstream.com/discord)
- Source and issues: [github.com/EulerStream/TikTok-Live-Api](https://github.com/EulerStream/TikTok-Live-Api)

## License

[MIT](https://github.com/EulerStream/TikTok-Live-Api/blob/master/LICENSE) © EulerStream
