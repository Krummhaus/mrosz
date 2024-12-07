# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code/app

# Copy the backend's requirements.txt and install dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the backend application code
COPY backend/app /code/app

# Install NGINX to serve static files
RUN apt-get update && apt-get install -y nginx

# Check if /etc/nginx exists and create if necessary (in case it's missing)
RUN mkdir -p /etc/nginx/conf.d

# Copy the custom nginx configuration to the correct directory
COPY frontend/nginx.conf /etc/nginx/conf.d/nginx.conf

# Copy the frontend files (HTML, CSS, JS) to the NGINX directory
COPY frontend /usr/share/nginx/html

# Expose both FastAPI port (8000) and NGINX port (80)
EXPOSE 8000 80

# Start Nginx and Uvicorn in the foreground
#CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload & nginx -g 'daemon off;'"]
CMD ["nginx", "-g", "daemon off;"]

