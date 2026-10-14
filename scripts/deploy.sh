#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SITE_DIR="${SITE_DIR:-$REPO_DIR/site}"
CONTENT_DIR="${CONTENT_DIR:-$REPO_DIR/source}"
QUARTZ_DIR="${QUARTZ_DIR:-$REPO_DIR/quartz}"

cd "$REPO_DIR"

QUARTZ_BUILD_DIR="$(mktemp -d "${TMPDIR:-/tmp}/chartroom-quartz.XXXXXX")"
cleanup() {
    rm -rf "$QUARTZ_BUILD_DIR"
}
trap cleanup EXIT

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

echo "==> Preparing isolated Quartz build"
cp -R "$QUARTZ_DIR/quartz" "$QUARTZ_BUILD_DIR/quartz"
cp "$QUARTZ_DIR/package.json" "$QUARTZ_BUILD_DIR/package.json"
if [ -f "$QUARTZ_DIR/package-lock.json" ]; then
    cp "$QUARTZ_DIR/package-lock.json" "$QUARTZ_BUILD_DIR/package-lock.json"
fi
ln -s "$QUARTZ_DIR/node_modules" "$QUARTZ_BUILD_DIR/node_modules"

echo "==> Generating static site"
(
    cd "$QUARTZ_BUILD_DIR"
    npm run quartz -- build \
        --directory "$CONTENT_DIR" \
        --output "$SITE_DIR"
)

echo "==> Static site created"
echo "    $SITE_DIR"

# Add the real destination when you are ready to publish. Keep this command
# commented until the SSH host and remote document root are confirmed.
# RSYNC_DEST="user@example.com:/path/to/chartroom/"
# rsync --archive --compress --human-readable "$SITE_DIR/" "$RSYNC_DEST"

echo "==> Ready to publish with rsync"
