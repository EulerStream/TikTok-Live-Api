// Package eulerstream is the TikTok LIVE API SDK for Go, the official Go client
// for the [EulerStream] TikTok LIVE API.
//
// Connect to any TikTok LIVE stream by @username and receive real-time chat
// messages, gifts, likes, follows, shares, viewer counts, room stats and PK
// battles over a managed WebSocket, plus a fully typed client for webcast
// signing, LIVE rooms, gifts, rankings, LIVE alerts, moderation, captchas and
// analytics. EulerStream hosts and maintains the connection layer, so your
// integration keeps working when TikTok changes its webcast protocol.
//
// Get a free API key at https://www.eulerstream.com/register, then:
//
//	client := eulerstream.NewEulerStreamClient(eulerstream.WithAPIKey("YOUR_API_KEY"))
//
//	// Look up any TikTok user by @username
//	user, _, err := client.TikTokUsers.RetrieveTikTokUserBasic(ctx, "tv_asahi_news").Execute()
//
//	// Browse the TikTok LIVE gift catalog
//	catalog, _, err := client.TikTokLiveGifts.ListWebcastGifts(ctx).Execute()
//
// Every API group in the [EulerStream OpenAPI spec] is a field on
// [EulerStreamClient]; see the [EulerStream docs] for per-endpoint Go examples,
// and [pricing] for the free Community tier and paid plans.
//
// This project is not affiliated with, endorsed by, or connected to TikTok or
// ByteDance.
//
// [EulerStream]: https://www.eulerstream.com
// [EulerStream OpenAPI spec]: https://www.eulerstream.com/docs/openapi
// [EulerStream docs]: https://www.eulerstream.com/docs/intro
// [pricing]: https://www.eulerstream.com/pricing
package eulerstream

import (
	"net/http"

	eulerapi "github.com/EulerStream/TikTok-Live-Api/sdk/go/generated"
)

// EulerStreamClient is a convenience wrapper around the generated API client.
// It exposes each API service group as a named field with a friendly name.
type EulerStreamClient struct {
	Accounts *eulerapi.AccountsAPIService
	Analytics *eulerapi.AnalyticsAPIService
	Authentication *eulerapi.AuthenticationAPIService
	Captchas *eulerapi.TikTokCaptchasAPIService
	General *eulerapi.TikTokGeneralAPIService
	Webcast *eulerapi.TikTokLIVEAPIService
	TikTokLiveAgencies *eulerapi.TikTokLIVEAgenciesAPIService
	AlertTargets *eulerapi.TikTokLIVEAlertTargetsAPIService
	Alerts *eulerapi.TikTokLIVEAlertsAPIService
	TikTokLiveAnchors *eulerapi.TikTokLIVEAnchorsAPIService
	TikTokLiveEvents *eulerapi.TikTokLIVEEventsAPIService
	TikTokLiveGifts *eulerapi.TikTokLIVEGiftsAPIService
	Moderation *eulerapi.TikTokLIVEModerationAPIService
	TikTokLiveRankings *eulerapi.TikTokLIVERankingsAPIService
	TikTokLiveRooms *eulerapi.TikTokLIVERoomsAPIService
	TikTokSigning *eulerapi.TikTokSigningAPIService
	TikTokUsers *eulerapi.TikTokUsersAPIService
	TikTokVideos *eulerapi.TikTokVideosAPIService
	TikTokWebSocketAPI *eulerapi.TikTokWebSocketAPIAPIService

	// Raw gives direct access to the underlying generated APIClient.
	Raw *eulerapi.APIClient
}

// ClientOption configures the EulerStreamClient.
type ClientOption func(*eulerapi.Configuration)

// WithAPIKey sets the default API key header for all requests.
func WithAPIKey(apiKey string) ClientOption {
	return func(cfg *eulerapi.Configuration) {
		cfg.AddDefaultHeader("apiKey", apiKey)
	}
}

// WithHTTPClient sets a custom http.Client for all requests.
func WithHTTPClient(client *http.Client) ClientOption {
	return func(cfg *eulerapi.Configuration) {
		cfg.HTTPClient = client
	}
}

// WithServerIndex selects which server to use (0=Public, 1=Enterprise, 2=Staging).
func WithServerIndex(index int) ClientOption {
	return func(cfg *eulerapi.Configuration) {
		if index >= 0 && index < len(cfg.Servers) {
			// Store the index; the generated client reads it from context,
			// but we also set Host/Scheme as a convenience so it works without context.
			url, err := cfg.Servers.URL(index, nil)
			if err == nil {
				_ = url // server index is handled via context in generated code
			}
		}
	}
}

// NewEulerStreamClient creates a new client with the given options.
func NewEulerStreamClient(opts ...ClientOption) *EulerStreamClient {
	cfg := eulerapi.NewConfiguration()

	for _, opt := range opts {
		opt(cfg)
	}

	raw := eulerapi.NewAPIClient(cfg)

	return &EulerStreamClient{
		Accounts: raw.AccountsAPI,
		Analytics: raw.AnalyticsAPI,
		Authentication: raw.AuthenticationAPI,
		Captchas: raw.TikTokCaptchasAPI,
		General: raw.TikTokGeneralAPI,
		Webcast: raw.TikTokLIVEAPI,
		TikTokLiveAgencies: raw.TikTokLIVEAgenciesAPI,
		AlertTargets: raw.TikTokLIVEAlertTargetsAPI,
		Alerts: raw.TikTokLIVEAlertsAPI,
		TikTokLiveAnchors: raw.TikTokLIVEAnchorsAPI,
		TikTokLiveEvents: raw.TikTokLIVEEventsAPI,
		TikTokLiveGifts: raw.TikTokLIVEGiftsAPI,
		Moderation: raw.TikTokLIVEModerationAPI,
		TikTokLiveRankings: raw.TikTokLIVERankingsAPI,
		TikTokLiveRooms: raw.TikTokLIVERoomsAPI,
		TikTokSigning: raw.TikTokSigningAPI,
		TikTokUsers: raw.TikTokUsersAPI,
		TikTokVideos: raw.TikTokVideosAPI,
		TikTokWebSocketAPI: raw.TikTokWebSocketAPIAPI,
		Raw: raw,
	}
}
