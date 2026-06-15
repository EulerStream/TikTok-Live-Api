echo "Fetching latest OpenAPI spec from EulerStream..."

mkdir -p build

# Get the spec
wget -O ./build/openapi.json https://api.eulerstream.com/dashboard/openapi

# Generate TypeScript
openapi-generator-cli generate -i ./build/openapi.json -g typescript-axios -o ./src/sdk

# Render the client wrapper from template
echo "Rendering index.ts from template..."
npx tsx ./render-template.ts
