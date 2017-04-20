# We us alpine as base image, since it is very small
FROM alpine

# apk is alpine package manager
RUN apk add --no-cache python3

# Copy the script in the root folder
COPY fizzbuzz_docker.py /

# Run command
CMD ["python3", "/fizzbuzz_docker.py", "20"]
