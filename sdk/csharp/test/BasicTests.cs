using System;
using System.Linq;
using System.Reflection;
using Xunit;
using EulerApiSdk;
using EulerApiSdk.Api;

namespace EulerApiSdk.Tests
{
    public class BasicTests : IDisposable
    {
        private readonly EulerStreamApiClient _client;

        public BasicTests()
        {
            _client = new EulerStreamApiClient();
        }

        public void Dispose()
        {
            _client.Dispose();
        }

        // The set of API groups is discovered dynamically: any public instance
        // property whose type is an interface in the EulerApiSdk.Api namespace is
        // an API group exposed by the client. Discovering them via reflection
        // (instead of hardcoding Accounts/Webcast/Premium/...) keeps these tests
        // in sync with the OpenAPI spec when API groups are added, renamed, or
        // removed.
        private static PropertyInfo[] ApiProperties() =>
            typeof(EulerStreamApiClient)
                .GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(p => p.PropertyType.IsInterface
                            && p.PropertyType.Namespace == "EulerApiSdk.Api")
                .ToArray();

        [Fact]
        public void Client_CanBeInstantiated()
        {
            Assert.NotNull(_client);
        }

        [Fact]
        public void Client_ImplementsIDisposable()
        {
            Assert.IsAssignableFrom<IDisposable>(_client);
        }

        [Fact]
        public void Client_ExposesApiProperties()
        {
            Assert.NotEmpty(ApiProperties());
        }

        [Fact]
        public void AllApiProperties_AreNonNullAndImplementTheirInterface()
        {
            foreach (var prop in ApiProperties())
            {
                var value = prop.GetValue(_client);
                Assert.True(value != null, $"{prop.Name} should not be null");
                Assert.True(
                    prop.PropertyType.IsInstanceOfType(value),
                    $"{prop.Name} should implement {prop.PropertyType.Name}");
            }
        }

        [Fact]
        public void Client_CanBeCreatedWithCustomBaseAddress()
        {
            using var customClient = new EulerStreamApiClient(baseAddress: "https://custom.example.com");
            Assert.NotNull(customClient);
        }

        [Fact]
        public void Client_CanBeDisposedMultipleTimes()
        {
            var client = new EulerStreamApiClient();
            client.Dispose();
            // Second dispose should not throw
            client.Dispose();
        }
    }
}
