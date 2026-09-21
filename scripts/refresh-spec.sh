#!/usr/bin/env bash
#
# Refresh both committed OpenAPI documents from the API server's source.
#
#   scripts/refresh-spec.sh /path/to/TikTok-Nest-Servers/servers/apps/euler-api-server
#
# Writes spec/openapi.json (the public document the public SDKs are generated
# from) and private/swagger.json (the full document the private SDK is
# generated from). Commit both, and bump the private submodule pointer once
# its commit is pushed.
set -euo pipefail

APP_DIR="${1:?usage: refresh-spec.sh <euler-api-server app directory>}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

[[ -f "$APP_DIR/scripts/emit-openapi.ts" ]] || { echo "error: $APP_DIR is not the euler-api-server app" >&2; exit 1; }

(cd "$APP_DIR" && pnpm run --silent openapi:emit -- --public) > "$ROOT_DIR/spec/openapi.json"
(cd "$APP_DIR" && pnpm run --silent openapi:emit) > "$ROOT_DIR/private/swagger.json"
python3 "$ROOT_DIR/.github/scripts/normalize_spec.py" "$ROOT_DIR/spec/openapi.json"

echo "spec/openapi.json:    $(python3 -c "import json;print(len(json.load(open('$ROOT_DIR/spec/openapi.json'))['paths']))") paths"
echo "private/swagger.json: $(python3 -c "import json;print(len(json.load(open('$ROOT_DIR/private/swagger.json'))['paths']))") paths"
