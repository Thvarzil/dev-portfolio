#!/bin/bash
set -e

echo "Collecting Django static files..."
cd backend
source venv/bin/activate
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build complete!"
