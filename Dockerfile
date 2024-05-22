# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app.py when the container launches
ENTRYPOINT ["streamlit", "run", "chatbot_v6.py", "--server.port=8501", "--server.address=0.0.0.0"]
