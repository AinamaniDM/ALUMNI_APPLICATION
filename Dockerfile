# Use Python 3.12 slim image as the base
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Install system dependencies (for compiling dependencies like psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Expose port (informational; Render uses $PORT)
EXPOSE 8000

# Run the app with Gunicorn, binding to Render’s assigned port
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} alumni_connect.wsgi:application"]