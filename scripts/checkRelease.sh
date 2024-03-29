#!/bin/bash

VERSION=$(grep VERSION "src/constants.py" | cut -d "=" -f 2 | sed 's/'\''//g' | sed 's/"//g' | sed 's/ //g' | sed 's/\r//')
echo "Current version: $VERSION"
echo "VERSION=$VERSION" >>"$GITHUB_OUTPUT"

REMOTE_VERSIONS=$(git ls-remote --tags -q | cut -d "/" -f 3)
echo "Remote versions: $REMOTE_VERSIONS"

for REMOTE_VERSION in $REMOTE_VERSIONS; do
    if [[ "$REMOTE_VERSION" == "$VERSION" ]]; then
        echo "Current version is already released."
        echo "CONTINUE=false" >>"$GITHUB_OUTPUT"
        exit 0
    fi
done

echo "CONTINUE=true" >>"$GITHUB_OUTPUT"

if [[ $VERSION == *"beta"* ]]; then
    echo "SET_PRE_RELEASE=true" >>"$GITHUB_OUTPUT"
else
    echo "SET_PRE_RELEASE=false" >>"$GITHUB_OUTPUT"
fi
