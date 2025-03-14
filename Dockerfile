FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files from the current directory into the container
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
