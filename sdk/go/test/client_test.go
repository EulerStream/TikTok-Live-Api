package eulerstream_test

import (
	"net/http"
	"reflect"
	"strings"
	"testing"

	eulerstream "github.com/EulerStream/TikTok-Live-Api/sdk/go"
)

func TestNewEulerStreamClient_NoOptions(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_WithAPIKey(t *testing.T) {
	client := eulerstream.NewEulerStreamClient(eulerstream.WithAPIKey("test-key"))
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_WithHTTPClient(t *testing.T) {
	custom := &http.Client{}
	client := eulerstream.NewEulerStreamClient(eulerstream.WithHTTPClient(custom))
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_WithMultipleOptions(t *testing.T) {
	client := eulerstream.NewEulerStreamClient(
		eulerstream.WithAPIKey("test-key"),
		eulerstream.WithHTTPClient(&http.Client{}),
		eulerstream.WithServerIndex(0),
	)
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_RawClientAccessible(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()
	if client.Raw == nil {
		t.Fatal("expected Raw (*eulerapi.APIClient) to be non-nil")
	}
}

// The API service fields are discovered dynamically via reflection: any struct
// field whose type is a *eulerapi.*APIService is an API group exposed by the
// client. Discovering them this way (instead of hardcoding Accounts/Webcast/
// Premium/...) keeps this test in sync with the OpenAPI spec when API groups are
// added, renamed, or removed.
func TestNewEulerStreamClient_AllServiceFieldsNonNil(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()

	v := reflect.ValueOf(client).Elem()
	tp := v.Type()
	found := 0
	for i := 0; i < tp.NumField(); i++ {
		field := tp.Field(i)
		if !strings.HasSuffix(field.Type.String(), "APIService") {
			continue
		}
		found++
		if v.Field(i).IsNil() {
			t.Errorf("expected service field %s to be non-nil", field.Name)
		}
	}

	if found == 0 {
		t.Fatal("expected at least one API service field on the client")
	}
}
