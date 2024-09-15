#!/bin/sh
# When you Update Version

BUILD_VERSION=$(python print_version.py)

git add __version__.py
git commit -m"Updated Version $BUILD_VERSION"
git push

# Specify the file to read from

git tag -a v${BUILD_VERSION} -m "Release version ${BUILD_VERSION}"
git push origin v${BUILD_VERSION}

echo "Building Frontend version ${BUILD_VERSION}"

docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:$BUILD_VERSION .

python ./update_k8s_manifest_version.py

./deploy-frontend-to-k8s.sh deploy


