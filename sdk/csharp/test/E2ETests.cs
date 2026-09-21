using System;
using System.Threading.Tasks;
using Xunit;
using EulerApiSdk;
using EulerApiSdk.Api;

namespace EulerApiSdk.Tests
{
    public class E2ETests : IDisposable
    {
        private readonly EulerStreamApiClient _client;

        public E2ETests()
        {
            _client = new EulerStreamApiClient();
        }

        public void Dispose()
        {
            _client.Dispose();
        }

        [Fact]
        public async Task GetHosts_ReturnsSuccessfulResponse()
        {
            var response = await _client.Analytics.GetHostsAsync();

            Assert.True(response.IsOk, "Expected a 200 OK response from /analytics/hosts");

            var hostsResponse = response.Ok();
            Assert.NotNull(hostsResponse);
            // Shape only, like the other languages' e2e tests: the list is empty whenever no peer is registered.
            Assert.NotNull(hostsResponse.Hosts);
        }
    }
}
