#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Fetching latest OpenAPI spec from EulerStream..."

mkdir -p "$SCRIPT_DIR/build"

# Get the spec
wget -O "$SCRIPT_DIR/build/openapi.json" https://api.eulerstream.com/dashboard/openapi

# Generate C# SDK
echo "Generating C# SDK..."
cd "$ROOT_DIR"
npx @openapitools/openapi-generator-cli generate \
  -i ./csharp-sdk/build/openapi.json \
  -g csharp \
  -o ./csharp-sdk/src/generated \
  --additional-properties=packageName=EulerApiSdk,targetFramework=net8.0,nullableReferenceTypes=true

# Fix enum member conflicts in generated code
echo "Fixing enum conflicts..."
npx tsx "$SCRIPT_DIR/fix-enum-conflicts.ts"

# Render the client wrapper from template
echo "Rendering EulerStreamApiClient.cs from template..."
npx tsx "$SCRIPT_DIR/render-template.ts"
