#!/bin/bash

# Specify the file to read from
BUILD_VERSION=$(python print_version.py)

echo "$BUILD_VERSION"

docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:$BUILD_VERSION .
