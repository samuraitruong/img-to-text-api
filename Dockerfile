# Use the official Python image as the base image
FROM python:3.9-slim
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  tesseract-ocr  libtesseract-dev  -y

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory to the container
COPY ./app ./app

# Expose the port that the Flask app will run on
EXPOSE 8080
EXPOSE 5000
WORKDIR /app/app
# Set the environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_PORT=8080

# Run the Flask app
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8080"]
