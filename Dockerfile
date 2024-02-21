# Use the official Python 3.8 image as a base
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Command to run on container start
CMD [ "python", "./app.py" ]
