#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Fetching latest OpenAPI spec from EulerStream..."
mkdir -p "$SCRIPT_DIR/build"
wget -O "$SCRIPT_DIR/build/openapi.json" https://api.eulerstream.com/dashboard/openapi

echo "Generating Go SDK..."
cd "$ROOT_DIR"
npx @openapitools/openapi-generator-cli generate \
  -i ./go-sdk/build/openapi.json \
  -g go \
  -o ./go-sdk/generated \
  --additional-properties=packageName=eulerapi,moduleName=github.com/EulerStream/Euler-Api-Sdk/go-sdk

# Remove the generated go.mod/go.sum — the root go-sdk/go.mod is the module root
rm -f ./go-sdk/generated/go.mod ./go-sdk/generated/go.sum

# Fix enum constant conflicts in generated code
echo "Fixing enum constant conflicts..."
npx tsx ./go-sdk/fix-enum-conflicts.ts

echo "Rendering client.go from template..."
npx tsx ./go-sdk/render-template.ts
