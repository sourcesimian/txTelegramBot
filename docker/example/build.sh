#!/bin/bash

proxy=$1

IMAGE=telegrambot

if [ -n "$proxy" ]; then
    ARGS="--build-arg http_proxy=http://$proxy --build-arg https_proxy=https://$proxy"
fi

if tar -czh . | docker build $ARGS - | tee build.log; then

    ID=$(tail -1 build.log | awk '{print $3;}')
    docker tag -f $ID ${IMAGE}:latest

    docker images | grep ${IMAGE}
else
    exit 1
fi
