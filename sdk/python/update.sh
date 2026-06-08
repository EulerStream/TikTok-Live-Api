echo "Fetching latest OpenAPI spec from EulerStream..."

mkdir -p "build"

# Get the spec
wget -O ./build/openapi.json https://tiktok.eulerstream.com/dashboard/openapi

# Generate Python
openapi-python-client generate \
  --url https://tiktok.eulerstream.com/dashboard/openapi \
  --output-path ./ \
  --overwrite \
  --config config.yaml

# Emit the test manifest from the freshly generated SDK
python scripts/render_manifest.py
