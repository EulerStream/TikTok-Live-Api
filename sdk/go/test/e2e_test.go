package eulerstream_test

import (
	"context"
	"net/http"
	"testing"

	eulerstream "github.com/EulerStream/TikTok-Live-Api/sdk/go"
)

func TestGetHosts_E2E(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()

	hosts, httpResp, err := client.Analytics.GetHosts(context.Background()).Execute()
	if err != nil {
		t.Fatalf("GetHosts returned error: %v", err)
	}

	if httpResp.StatusCode != http.StatusOK {
		t.Fatalf("expected status 200, got %d", httpResp.StatusCode)
	}

	if hosts == nil {
		t.Fatal("expected non-nil HostsResponse, got nil")
	}
}
