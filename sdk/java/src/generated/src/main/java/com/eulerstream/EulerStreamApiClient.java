package com.eulerstream;

import com.eulerstream.api.AccountsApi;
import com.eulerstream.api.AnalyticsApi;
import com.eulerstream.api.AuthenticationApi;
import com.eulerstream.api.TikTokCaptchasApi;
import com.eulerstream.api.TikTokGeneralApi;
import com.eulerstream.api.TikTokLiveAlertTargetsApi;
import com.eulerstream.api.TikTokLiveAlertsApi;
import com.eulerstream.api.TikTokLiveAnchorsApi;
import com.eulerstream.api.TikTokLiveApi;
import com.eulerstream.api.TikTokLiveGiftsApi;
import com.eulerstream.api.TikTokLiveModerationApi;
import com.eulerstream.api.TikTokLiveRoomsApi;
import com.eulerstream.api.TikTokWebSocketApiApi;

/**
 * EulerStream API Client
 *
 * <p>A convenience wrapper that aggregates all generated API classes into a single client.
 * Supports a builder pattern for idiomatic Java configuration.</p>
 *
 * <pre>{@code
 * EulerStreamApiClient client = EulerStreamApiClient.builder()
 *     .apiKey("your-api-key")
 *     .build();
 *
 * // Use the client
 * client.webcast().signWebcastUrl(...);
 * }</pre>
 */
public class EulerStreamApiClient {

    private final ApiClient apiClient;

    private final AccountsApi accounts;
    private final AnalyticsApi analytics;
    private final AuthenticationApi authentication;
    private final TikTokCaptchasApi captchas;
    private final TikTokGeneralApi general;
    private final TikTokLiveAlertTargetsApi alertTargets;
    private final TikTokLiveAlertsApi alerts;
    private final TikTokLiveAnchorsApi tikTokLiveAnchors;
    private final TikTokLiveApi webcast;
    private final TikTokLiveGiftsApi tikTokLiveGifts;
    private final TikTokLiveModerationApi moderation;
    private final TikTokLiveRoomsApi tikTokLiveRooms;
    private final TikTokWebSocketApiApi tikTokWebSocketApi;

    private EulerStreamApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;

        // Initialize API instances
        this.accounts = new AccountsApi(apiClient);
        this.analytics = new AnalyticsApi(apiClient);
        this.authentication = new AuthenticationApi(apiClient);
        this.captchas = new TikTokCaptchasApi(apiClient);
        this.general = new TikTokGeneralApi(apiClient);
        this.alertTargets = new TikTokLiveAlertTargetsApi(apiClient);
        this.alerts = new TikTokLiveAlertsApi(apiClient);
        this.tikTokLiveAnchors = new TikTokLiveAnchorsApi(apiClient);
        this.webcast = new TikTokLiveApi(apiClient);
        this.tikTokLiveGifts = new TikTokLiveGiftsApi(apiClient);
        this.moderation = new TikTokLiveModerationApi(apiClient);
        this.tikTokLiveRooms = new TikTokLiveRoomsApi(apiClient);
        this.tikTokWebSocketApi = new TikTokWebSocketApiApi(apiClient);
    }

    /**
     * Get the underlying ApiClient for advanced configuration.
     *
     * @return the ApiClient instance
     */
    public ApiClient getApiClient() {
        return apiClient;
    }

    /**
     * Get the AccountsApi instance.
     *
     * @return the AccountsApi
     */
    public AccountsApi accounts() {
        return accounts;
    }

    /**
     * Get the AnalyticsApi instance.
     *
     * @return the AnalyticsApi
     */
    public AnalyticsApi analytics() {
        return analytics;
    }

    /**
     * Get the AuthenticationApi instance.
     *
     * @return the AuthenticationApi
     */
    public AuthenticationApi authentication() {
        return authentication;
    }

    /**
     * Get the TikTokCaptchasApi instance.
     *
     * @return the TikTokCaptchasApi
     */
    public TikTokCaptchasApi captchas() {
        return captchas;
    }

    /**
     * Get the TikTokGeneralApi instance.
     *
     * @return the TikTokGeneralApi
     */
    public TikTokGeneralApi general() {
        return general;
    }

    /**
     * Get the TikTokLiveAlertTargetsApi instance.
     *
     * @return the TikTokLiveAlertTargetsApi
     */
    public TikTokLiveAlertTargetsApi alertTargets() {
        return alertTargets;
    }

    /**
     * Get the TikTokLiveAlertsApi instance.
     *
     * @return the TikTokLiveAlertsApi
     */
    public TikTokLiveAlertsApi alerts() {
        return alerts;
    }

    /**
     * Get the TikTokLiveAnchorsApi instance.
     *
     * @return the TikTokLiveAnchorsApi
     */
    public TikTokLiveAnchorsApi tikTokLiveAnchors() {
        return tikTokLiveAnchors;
    }

    /**
     * Get the TikTokLiveApi instance.
     *
     * @return the TikTokLiveApi
     */
    public TikTokLiveApi webcast() {
        return webcast;
    }

    /**
     * Get the TikTokLiveGiftsApi instance.
     *
     * @return the TikTokLiveGiftsApi
     */
    public TikTokLiveGiftsApi tikTokLiveGifts() {
        return tikTokLiveGifts;
    }

    /**
     * Get the TikTokLiveModerationApi instance.
     *
     * @return the TikTokLiveModerationApi
     */
    public TikTokLiveModerationApi moderation() {
        return moderation;
    }

    /**
     * Get the TikTokLiveRoomsApi instance.
     *
     * @return the TikTokLiveRoomsApi
     */
    public TikTokLiveRoomsApi tikTokLiveRooms() {
        return tikTokLiveRooms;
    }

    /**
     * Get the TikTokWebSocketApiApi instance.
     *
     * @return the TikTokWebSocketApiApi
     */
    public TikTokWebSocketApiApi tikTokWebSocketApi() {
        return tikTokWebSocketApi;
    }

    /**
     * Create a new builder for EulerStreamApiClient.
     *
     * @return a new Builder instance
     */
    public static Builder builder() {
        return new Builder();
    }

    /**
     * Create a client with default configuration (no API key).
     *
     * @return a new EulerStreamApiClient with default settings
     */
    public static EulerStreamApiClient createDefault() {
        return new Builder().build();
    }

    /**
     * Builder for {@link EulerStreamApiClient}.
     */
    public static class Builder {

        private String basePath = "https://api.eulerstream.com";
        private String apiKey;
        private ApiClient apiClient;

        private Builder() {}

        /**
         * Set the base path (URL) for API requests.
         *
         * @param basePath the base URL
         * @return this builder
         */
        public Builder basePath(String basePath) {
            this.basePath = basePath;
            return this;
        }

        /**
         * Set the API key for authentication.
         *
         * @param apiKey the API key
         * @return this builder
         */
        public Builder apiKey(String apiKey) {
            this.apiKey = apiKey;
            return this;
        }

        /**
         * Provide a fully-configured ApiClient instance.
         * When set, basePath and apiKey on this builder are ignored.
         *
         * @param apiClient the pre-configured ApiClient
         * @return this builder
         */
        public Builder apiClient(ApiClient apiClient) {
            this.apiClient = apiClient;
            return this;
        }

        /**
         * Build the EulerStreamApiClient.
         *
         * @return a configured EulerStreamApiClient
         */
        public EulerStreamApiClient build() {
            ApiClient client = this.apiClient;
            if (client == null) {
                client = new ApiClient();
                client.setBasePath(this.basePath);
                if (this.apiKey != null) {
                    client.setApiKey(this.apiKey);
                }
            }
            return new EulerStreamApiClient(client);
        }
    }
}
