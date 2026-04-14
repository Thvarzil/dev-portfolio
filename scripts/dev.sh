#!/bin/bash
echo "Starting Django backend..."
cd backend
source venv/bin/activate
python manage.py runserver
