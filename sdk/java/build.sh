#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Fetching latest OpenAPI spec from EulerStream..."

mkdir -p "$SCRIPT_DIR/build"

# Get the spec
wget -O "$SCRIPT_DIR/build/openapi.json" https://api.eulerstream.com/dashboard/openapi

# Generate Java SDK
echo "Generating Java SDK..."
cd "$SCRIPT_DIR"
rm -rf ./src/generated
npx @openapitools/openapi-generator-cli generate \
  -i ./build/openapi.json \
  -g java \
  -o ./src/generated \
  --additional-properties=groupId=com.eulerstream,artifactId=euler-api-sdk,apiPackage=com.eulerstream.api,modelPackage=com.eulerstream.model,invokerPackage=com.eulerstream

# Render the client wrapper from template
echo "Rendering EulerStreamApiClient.java from template..."
npx tsx ./scripts/render-template.ts

# Patch the generated pom for Maven Central publishing (com.eulerstream)
echo "Patching pom for Maven Central..."
npx tsx ./scripts/fix-pom.ts
