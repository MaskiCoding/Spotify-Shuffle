# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN apt-get update && apt-get install -y binutils
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pyinstaller

# Run PyInstaller to create the executable
RUN pyinstaller --onefile --windowed main.py

# Keep the container running for inspection
CMD ["tail", "-f", "/dev/null"]

# Label to specify the author
LABEL maintainer="Maximilian Lin <MaximilianLin@vivaldi.net>"