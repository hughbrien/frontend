#!/bin/sh
#Update Version

# Specify the file to read from
BUILD_VERSION=$(python print_version.py)

echo "Building Frontend version ${BUILD_VERSION}"

docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:$BUILD_VERSION .

python ./update_k8s_manifest_version.py

./deploy-frontend-to-k8s.sh deploy


