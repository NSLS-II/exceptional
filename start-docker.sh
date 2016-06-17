#!/bin/bash

mkdir -p /tmp/data
DOCKER_IMAGE="ericdill/exceptional"


docker run -p 5000:5000 \
    -v /tmp/data:/data \
    -e DB_PATH="/data/db.json" \
    -e SLACK_TOKEN=`cat ~/dev/dotfiles/tokens/edill.slack` \
    -d \
    "ericdill/exceptional"
