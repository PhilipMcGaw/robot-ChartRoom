#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SITE_DIR="${SITE_DIR:-$REPO_DIR/site}"
MKDOCS_BIN="${MKDOCS_BIN:-$REPO_DIR/.venv/bin/mkdocs}"

cd "$REPO_DIR"

echo "==> Building Chartroom static site"

if [ ! -x "$MKDOCS_BIN" ]; then
    if command -v mkdocs >/dev/null 2>&1; then
        MKDOCS_BIN="$(command -v mkdocs)"
    else
        echo "ERROR: MkDocs was not found."
        echo "       Install it in $REPO_DIR/.venv or set MKDOCS_BIN."
        exit 1
    fi
fi

"$MKDOCS_BIN" build --clean --strict --site-dir "$SITE_DIR"

echo "==> Static site created"
echo "    $SITE_DIR"

# Add the real destination when you are ready to publish. Keep this command
# commented until the SSH host and remote document root are confirmed.
# RSYNC_DEST="user@example.com:/path/to/chartroom/"
# rsync --archive --compress --human-readable "$SITE_DIR/" "$RSYNC_DEST"

echo "==> Ready to publish with rsync"
