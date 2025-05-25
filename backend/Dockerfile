# Use slim Python base image for smaller size
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Create static directory (optional, if using collectstatic)
RUN mkdir -p /app/static

# Collect static files (can be skipped if using S3 only)
RUN #python manage.py collectstatic --noinput

# Expose port for ASGI
EXPOSE 8000

# Default command for running Daphne (ASGI)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]
