# Use Python 3.12 slim image as the base
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
# Copy and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

EXPOSE 8000

# Run the app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "alumni_connect.wsgi:application","alumni-connect-n1w3.onrender.com"]
#CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]