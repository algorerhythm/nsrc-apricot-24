# Use the official Python 3.8 image as a base
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY app.py .

# Command to run on container start
CMD [ "python", "./app.py" ]
