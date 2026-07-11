# google-site-verification: google93ecefd594fb7167.html

3rd-Party TikTok LIVE API Client - The #1 Worldwide freemium SaaS API for TikTok LIVE data retrieval, offered in all major languages! Official SDK libraries for the [EulerStream](https://www.eulerstream.com) TikTok LIVE API.

google-site-verification: google93ecefd594fb7167.html

<p>
    google-site-verification: google93ecefd594fb7167.html
</p>

[![Stars](https://img.shields.io/github/stars/EulerStream/EulerApiSdk?style=flat&color=0274b5)](https://github.com/EulerStream/EulerApiSdk)
[![Issues](https://img.shields.io/github/issues/EulerStream/EulerApiSdk)](https://github.com/EulerStream/EulerApiSdk/issues)
[![Patrons](https://www.eulerstream.com/api/pips/patrons?v=002)](https://www.eulerstream.com/)

## SDKs

| Language | Package | Install |
|----------|---------|---------|
| TypeScript | [`@eulerstream/euler-api-sdk`](https://www.npmjs.com/package/@eulerstream/euler-api-sdk) | `npm i @eulerstream/euler-api-sdk` |
| Python | [`EulerApiSdk`](https://pypi.org/project/EulerApiSdk/) | `pip install EulerApiSdk` |
| C# | [`EulerApiSdk`](https://www.nuget.org/packages/EulerApiSdk) | `dotnet add package EulerApiSdk` |
| Java | [`io.github.isaackogan:euler-api-sdk`](https://central.sonatype.com/artifact/io.github.isaackogan/euler-api-sdk) | Maven / Gradle |
| Go | [`github.com/EulerStream/TikTok-Live-Api/sdk/go`](https://pkg.go.dev/github.com/EulerStream/TikTok-Live-Api/sdk/go) | `go get github.com/EulerStream/TikTok-Live-Api/sdk/go` |

> [!TIP]
> Full API documentation and the interactive OpenAPI spec are available at [eulerstream.com/docs/openapi](https://www.eulerstream.com/docs/openapi).

## Quick Start

### TypeScript

```ts
import EulerStreamApiClient from "@eulerstream/euler-api-sdk";

const client = new EulerStreamApiClient({ apiKey: "YOUR_API_KEY" });

// Fetch a TikTok LIVE webcast URL
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
> See the full SDK documentation for each language:
> - [TypeScript SDK](./typescript-sdk/README.md)
> - [Python SDK](./python-sdk/README.md)
> - [C# SDK](./csharp-sdk/)
> - [Java SDK](./java-sdk/)
> - [Go SDK](./sdk/go/)

## CI / Release Pipeline

SDKs are auto-generated from the [EulerStream OpenAPI spec](https://www.eulerstream.com/docs/openapi) via GitHub Actions.

| Workflow | Purpose |
|----------|---------|
| **Dry Run** | Generate & build SDKs without publishing (validation only) |
| **Release** | Generate, version, and publish to npm / PyPI / NuGet / Maven Central / Go tags |

> [!IMPORTANT]
> Releases are triggered manually via the GitHub Actions **"Run workflow"** button — no automatic publishing on push.

## Enterprise

<table>
<tr>
    <td><br/><img width="180px" src="https://raw.githubusercontent.com/isaackogan/TikTokLive/master/.github/SquareLogo.png"><br/><br/></td>
    <td>
        <a href="https://www.eulerstream.com">
            <strong>EulerStream</strong> — managed TikTok LIVE WebSocket connections, increased access, LIVE alerts, JWT auth, and more.
        </a>
    </td>
</tr>
</table>

google-site-verification: google93ecefd594fb7167.html

## Community

Questions, issues, or feedback? Join the [EulerStream Discord](https://www.eulerstream.com/discord).

## License

[MIT](./LICENSE)
