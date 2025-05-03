# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir reduces image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 8080 available
EXPOSE 8080

# Define environment variable for the port
ENV PORT=8080

# Command to run the application using Gunicorn (Shell form)
CMD gunicorn --bind "0.0.0.0:$PORT" app:app
