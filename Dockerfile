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

# Copy the rest of the application code (app.py, index.html, static folder)
# from your local machine to the container at /app
COPY . .

# Make port 8080 available to the world outside this container
# Cloud Run uses the PORT environment variable, but this is good practice
EXPOSE 8080

# Define environment variable for the port (Cloud Run will override this)
ENV PORT 8080

# Command to run the application using Gunicorn
# It binds to all interfaces (0.0.0.0) on the specified port ($PORT)
# app:app means run the 'app' object from the 'app.py' module
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]