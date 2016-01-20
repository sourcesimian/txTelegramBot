#!/bin/bash

proxy=$1

docker run -it -v $PWD/config.ini:/home/telegrambot/config.ini telegrambot