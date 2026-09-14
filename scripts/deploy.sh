#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SITE_DIR="${SITE_DIR:-$REPO_DIR/site}"
CONTENT_DIR="${CONTENT_DIR:-$REPO_DIR/docs}"
QUARTZ_DIR="${QUARTZ_DIR:-$REPO_DIR/quartz}"

cd "$REPO_DIR"

echo "==> Building Chartroom static site with Quartz"

if [ ! -d "$CONTENT_DIR" ]; then
    echo "ERROR: Content directory not found: $CONTENT_DIR"
    exit 1
fi

if [ ! -f "$QUARTZ_DIR/package.json" ]; then
    echo "ERROR: Quartz checkout not found: $QUARTZ_DIR"
    exit 1
fi

if ! command -v node >/dev/null 2>&1 || ! command -v npm >/dev/null 2>&1; then
    echo "ERROR: Quartz requires Node.js and npm."
    exit 1
fi

if [ ! -x "$QUARTZ_DIR/node_modules/.bin/quartz" ]; then
    echo "==> Installing Quartz dependencies"
    npm --prefix "$QUARTZ_DIR" ci
fi

echo "==> Generating static site"
npm --prefix "$QUARTZ_DIR" exec -- quartz build \
    --directory "$CONTENT_DIR" \
    --output "$SITE_DIR"

echo "==> Static site created"
echo "    $SITE_DIR"

# Add the real destination when you are ready to publish. Keep this command
# commented until the SSH host and remote document root are confirmed.
# RSYNC_DEST="user@example.com:/path/to/chartroom/"
# rsync --archive --compress --human-readable "$SITE_DIR/" "$RSYNC_DEST"

echo "==> Ready to publish with rsync"
