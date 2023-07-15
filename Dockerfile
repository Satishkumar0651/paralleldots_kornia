# Use a lightweight base image
FROM jjanzic/docker-python3-opencv
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

ENV PORT 80

# Set the entrypoint command
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app