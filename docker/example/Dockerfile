FROM debian

ENV http_proxy=${http_proxy}
ENV https_proxy=${https_proxy}

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip
RUN apt-get update && apt-get install -y python3-openssl python3-requests
RUN pip3 install python-dateutil Twisted

RUN pip3 install https://github.com/sourcesimian/pyTelegramBotAPI/tarball/v0.2#egg=TelegramBotAPI-0.2
RUN pip3 install https://github.com/sourcesimian/pyPlugin/tarball/v0.1.1#egg=pyplugin-0.1.1

RUN useradd -ms /bin/bash telegrambot
USER telegrambot
WORKDIR /home/telegrambot/
COPY home /home/telegrambot/

ENTRYPOINT twistd -n telegrambot -c config.ini
STOPSIGNAL SIGTERM