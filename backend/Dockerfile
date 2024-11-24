# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /code

# Copy requirements and install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy application code to container
COPY ./app /code/app

# Expose the default FastAPI port
EXPOSE 8000

# Command to run the application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
