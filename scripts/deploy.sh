#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
PUBLIC_DIR="$HOME/public_html/chartroom_philipmcgaw_com"
VENV="$REPO_DIR/.venv"

cd "$REPO_DIR"

echo "==> Building Chartroom"

if [ ! -x "$VENV/bin/mkdocs" ]; then
    echo "ERROR: MkDocs virtual environment not found:"
    echo "       $VENV"
    exit 1
fi

"$VENV/bin/mkdocs" build --clean

echo "==> Publishing site"

mkdir -p "$PUBLIC_DIR"

# Remove the previous published site.
find "$PUBLIC_DIR" -mindepth 1 -maxdepth 1 -exec rm -rf {} +

# Copy the newly built site.
cp -a "$REPO_DIR/site/." "$PUBLIC_DIR/"

echo "==> Chartroom deployed"
echo "    https://chartroom.philipmcgaw.com/"
