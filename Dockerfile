# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files first (for better caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app

# Use a non-root user for security
RUN useradd -m myuser
USER myuser

# Expose the application port
EXPOSE 5000

# Define the default command to run your application
ENTRYPOINT ["python", "app.py"]
