# Start from a base image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app/

# Copy the requirements file into the container
COPY ./requirements.txt .

# Update the package index and install necessary packages
RUN apk update \
    && apk add --no-cache \
        gcc \
        musl-dev \ 
        python3-dev \
        g++ \
    && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the application
CMD [ "python", "app.py" ]
