#!/bin/bash
set -e

REPO="$(cd "$(dirname "$0")/.." && pwd)"
VENV=$REPO/venv

# Build side projects
echo "Building side projects..."
for dir in "$REPO"/side-projects/*/; do
    if [ -f "$dir/package.json" ]; then
        echo "  Building $dir..."
        (cd "$dir" && npm ci && npm run build)
    fi
done

echo "Collecting Django static files..."
"$VENV/bin/python" "$REPO/backend/manage.py" collectstatic --noinput

echo "Running migrations..."
"$VENV/bin/python" "$REPO/backend/manage.py" migrate --noinput

echo "Build complete!"
