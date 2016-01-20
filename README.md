# TelegramBot Service (unofficial) in Twisted Python3

A [Twisted](https://twistedmatrix.com) service that connects to the [Telegram Bot API](https://core.telegram.org/bots/api) using
[pyTelegramBotAPI](https://github.com/sourcesimian/pyTelegramBotAPI).

## Installation
```
pip install https://github.com/sourcesimian/pyTelegramBot/tarball/v0.1#egg=TelegramBot-0.1
```

## Usage
* Configure your Telegram Bot API Token in [```docker/example/config.ini```](/docker/example/config.ini) and also in 
[```tests/env.py```](tests/env.py) if you wish to run the tests.
* Write a plugin and put it in [```/plugins```](/plugins), or simply use the current examples.
* Now run in either the virtualenv or in a [Docker](https://www.docker.com/) container.
  * Virtualenv
    ```
    $ ./setup_env.sh
    $ . ./virtualenv/bin/activate
    $ twistd -n telegrambot -c docker/example/config.ini
    ```

  * Docker
    ```
    $ cd docker/example
    $ ./build.sh [<proxy-address>:<proxy-port>]
    $ ./run.sh
    ```
