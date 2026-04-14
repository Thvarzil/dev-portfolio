#!/bin/bash
# Run this on the Pi to deploy or update the portfolio.
# Usage: ./deploy/deploy.sh
set -e

REPO=/srv/portfolio
VENV=$REPO/venv
APP=$REPO/backend

echo "==> Pulling latest code..."
git -C "$REPO" pull

echo "==> Installing Python dependencies..."
"$VENV/bin/pip" install -q -r "$APP/requirements.txt"

echo "==> Running migrations..."
cd "$APP"
"$VENV/bin/python" manage.py migrate --noinput

echo "==> Collecting static files..."
"$VENV/bin/python" manage.py collectstatic --noinput

echo "==> Reloading gunicorn..."
sudo systemctl reload portfolio-gunicorn

echo "==> Done. Site is live at https://thvarzil.dev"
