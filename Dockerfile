# Python base image
FROM python:3.12-slim

# Prevents .pyc files and ensures real-time logs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first (cache optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Expose port 8000
EXPOSE 8000

# Default command on startup
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]