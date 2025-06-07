ocker# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY calculator.py .

# Run the python script
CMD ["python", "calculator.py"]