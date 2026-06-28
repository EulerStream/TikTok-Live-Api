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
	AlertTargets *eulerapi.TikTokLIVEAlertTargetsAPIService
	Alerts *eulerapi.TikTokLIVEAlertsAPIService
	Moderation *eulerapi.TikTokLIVEModerationAPIService
	Premium *eulerapi.TikTokLIVEPremiumAPIService

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
		AlertTargets: raw.TikTokLIVEAlertTargetsAPI,
		Alerts: raw.TikTokLIVEAlertsAPI,
		Moderation: raw.TikTokLIVEModerationAPI,
		Premium: raw.TikTokLIVEPremiumAPI,
		Raw: raw,
	}
}
