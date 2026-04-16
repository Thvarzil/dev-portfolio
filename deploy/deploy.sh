#!/bin/bash
# Run this on the Pi to deploy or update the portfolio.
# Usage: ./deploy/deploy.sh
set -e

REPO=/srv/portfolio
VENV=$REPO/venv
APP=$REPO/backend

echo "==> Pulling latest code..."
git -C "$REPO" pull
git -C "$REPO" submodule update --init --recursive

echo "==> Installing Python dependencies..."
"$VENV/bin/pip" install -q -r "$APP/requirements.txt"

echo "==> Building..."
bash "$REPO/scripts/build.sh"

echo "==> Reloading gunicorn..."
sudo systemctl reload portfolio-gunicorn

echo "==> Done. Site is live at https://thvarzil.dev"
