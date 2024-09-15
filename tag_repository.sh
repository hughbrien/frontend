#!/bin/bash

# Extract version from __version__.py
VERSION=$(python -c 'exec(open("__version__.py").read()); print(__version__)')

# Check if VERSION is not empty
if [ -z "$VERSION" ]; then
  echo "Version not found in __version__.py"
  exit 1
fi

# Create a Git tag using the extracted version
git tag -a "v$VERSION" -m "Release version $VERSION"

# Push the tag to the remote repository
git push origin "v$VERSION"