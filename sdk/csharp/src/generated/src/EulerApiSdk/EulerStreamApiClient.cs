#nullable enable

using System;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using EulerApiSdk.Api;
using EulerApiSdk.Client;
using EulerApiSdk.Extensions;

namespace EulerApiSdk
{
    /// <summary>
    /// EulerStream API Client — a convenient wrapper that exposes all generated
    /// API groups as properties and manages the underlying DI container.
    /// </summary>
    public sealed class EulerStreamApiClient : IDisposable
    {
        private readonly ServiceProvider _serviceProvider;

        /// <summary>
        /// Accounts API group.
        /// </summary>
        public IAccountsApi Accounts { get; }

        /// <summary>
        /// Analytics API group.
        /// </summary>
        public IAnalyticsApi Analytics { get; }

        /// <summary>
        /// Authentication API group.
        /// </summary>
        public IAuthenticationApi Authentication { get; }

        /// <summary>
        /// Captchas API group.
        /// </summary>
        public ITikTokCaptchasApi Captchas { get; }

        /// <summary>
        /// General API group.
        /// </summary>
        public ITikTokGeneralApi General { get; }

        /// <summary>
        /// TikTokLiveAgencies API group.
        /// </summary>
        public ITikTokLIVEAgenciesApi TikTokLiveAgencies { get; }

        /// <summary>
        /// AlertTargets API group.
        /// </summary>
        public ITikTokLIVEAlertTargetsApi AlertTargets { get; }

        /// <summary>
        /// Alerts API group.
        /// </summary>
        public ITikTokLIVEAlertsApi Alerts { get; }

        /// <summary>
        /// TikTokLiveAnchors API group.
        /// </summary>
        public ITikTokLIVEAnchorsApi TikTokLiveAnchors { get; }

        /// <summary>
        /// Webcast API group.
        /// </summary>
        public ITikTokLIVEApi Webcast { get; }

        /// <summary>
        /// TikTokLiveEvents API group.
        /// </summary>
        public ITikTokLIVEEventsApi TikTokLiveEvents { get; }

        /// <summary>
        /// TikTokLiveGifts API group.
        /// </summary>
        public ITikTokLIVEGiftsApi TikTokLiveGifts { get; }

        /// <summary>
        /// Moderation API group.
        /// </summary>
        public ITikTokLIVEModerationApi Moderation { get; }

        /// <summary>
        /// TikTokLiveRankings API group.
        /// </summary>
        public ITikTokLIVERankingsApi TikTokLiveRankings { get; }

        /// <summary>
        /// TikTokLiveRooms API group.
        /// </summary>
        public ITikTokLIVERoomsApi TikTokLiveRooms { get; }

        /// <summary>
        /// TikTokSigning API group.
        /// </summary>
        public ITikTokSigningApi TikTokSigning { get; }

        /// <summary>
        /// TikTokUsers API group.
        /// </summary>
        public ITikTokUsersApi TikTokUsers { get; }

        /// <summary>
        /// TikTokVideos API group.
        /// </summary>
        public ITikTokVideosApi TikTokVideos { get; }

        /// <summary>
        /// TikTokWebSocketAPI API group.
        /// </summary>
        public ITikTokWebSocketAPIApi TikTokWebSocketAPI { get; }

        /// <summary>
        /// Creates a new EulerStream API Client.
        /// </summary>
        /// <param name="configure">
        /// Optional callback to customise the <see cref="HostConfiguration"/>
        /// (e.g. add tokens, override HttpClient settings).
        /// </param>
        /// <param name="baseAddress">
        /// Override the default base address for API requests.
        /// </param>
        public EulerStreamApiClient(
            Action<HostConfiguration>? configure = null,
            string? baseAddress = null)
        {
            var services = new ServiceCollection();

            // Add logging (required by the generated API classes)
            services.AddLogging(builder => builder.AddConsole().SetMinimumLevel(LogLevel.Warning));

            // Register the generated SDK services
            services.AddApi(host =>
            {
                host.AddApiHttpClients(client =>
                {
                    client.BaseAddress = new Uri(baseAddress ?? ClientUtils.BASE_ADDRESS);
                });

                // Register a default placeholder API key token so the DI container
                // can always resolve TokenProvider<ApiKeyToken>.  When the caller
                // supplies real tokens via the configure callback, the later
                // registration wins (Microsoft DI last-wins semantics).
                host.AddTokens(new ApiKeyToken("", ClientUtils.ApiKeyHeader.ApiKey, prefix: ""));

                // Allow the caller to further configure (e.g. add tokens)
                configure?.Invoke(host);
            });

            _serviceProvider = services.BuildServiceProvider();

            // Resolve API instances
            Accounts = _serviceProvider.GetRequiredService<IAccountsApi>();
            Analytics = _serviceProvider.GetRequiredService<IAnalyticsApi>();
            Authentication = _serviceProvider.GetRequiredService<IAuthenticationApi>();
            Captchas = _serviceProvider.GetRequiredService<ITikTokCaptchasApi>();
            General = _serviceProvider.GetRequiredService<ITikTokGeneralApi>();
            TikTokLiveAgencies = _serviceProvider.GetRequiredService<ITikTokLIVEAgenciesApi>();
            AlertTargets = _serviceProvider.GetRequiredService<ITikTokLIVEAlertTargetsApi>();
            Alerts = _serviceProvider.GetRequiredService<ITikTokLIVEAlertsApi>();
            TikTokLiveAnchors = _serviceProvider.GetRequiredService<ITikTokLIVEAnchorsApi>();
            Webcast = _serviceProvider.GetRequiredService<ITikTokLIVEApi>();
            TikTokLiveEvents = _serviceProvider.GetRequiredService<ITikTokLIVEEventsApi>();
            TikTokLiveGifts = _serviceProvider.GetRequiredService<ITikTokLIVEGiftsApi>();
            Moderation = _serviceProvider.GetRequiredService<ITikTokLIVEModerationApi>();
            TikTokLiveRankings = _serviceProvider.GetRequiredService<ITikTokLIVERankingsApi>();
            TikTokLiveRooms = _serviceProvider.GetRequiredService<ITikTokLIVERoomsApi>();
            TikTokSigning = _serviceProvider.GetRequiredService<ITikTokSigningApi>();
            TikTokUsers = _serviceProvider.GetRequiredService<ITikTokUsersApi>();
            TikTokVideos = _serviceProvider.GetRequiredService<ITikTokVideosApi>();
            TikTokWebSocketAPI = _serviceProvider.GetRequiredService<ITikTokWebSocketAPIApi>();
        }

        /// <inheritdoc />
        public void Dispose()
        {
            _serviceProvider.Dispose();
        }
    }
}
