#!/bin/bash

echo "🚀 Starting Django application..."

# Wait for PostgreSQL to be ready.
echo "⏳ Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "✅ PostgreSQL ready!"

# Run migrations
echo "📦 Running migrations..."
python  manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python  manage.py collectstatic --noinput

# Create a superuser if one does not exist.
echo "👤 Creating superuser..."
python  shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superuser created: admin/admin123')
else:
    print('ℹ️ Superuser already exists')
END

# Start Gunicorn
echo "🦄 Starting Gunicorn..."
exec gunicorn setup.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 30 \
    --log-level info \
    --access-logfile - \
    --error-logfile -