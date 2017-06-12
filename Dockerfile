# We use alpine as base image, since it has a small footprint
FROM alpine

# apk is alpines package manager - invoked with RUN
RUN apk add --no-cache python3

# Copy the script in the root folder
COPY fizzbuzz_docker.py /

# Run this command when the container is started
CMD ["python3", "/fizzbuzz_docker.py", "20"]
