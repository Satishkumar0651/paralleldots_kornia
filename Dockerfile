# Use a lightweight base image
FROM python:3.8-slim-buster
# Install build dependencies
RUN apt-get update && \
    apt-get install -y gcc python3-dev libgl1-mesa-glx
RUN apt update; apt install -y libgl1
# Set the working directory
WORKDIR /app
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .



# Expose the port
EXPOSE 8000

# Set the entrypoint command
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
