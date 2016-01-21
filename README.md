# TelegramBot Service (unofficial) in Twisted Python3

A [Twisted](https://twistedmatrix.com) service that connects to the
[Telegram Bot API](https://core.telegram.org/bots/api) using
[TelegramBotAPI](https://github.com/sourcesimian/pyTelegramBotAPI).

## Installation
```
pip3 install txTelegramBot
```

## Usage
* Create a ```config.ini``` as follows, and set it up with your
[Telegram Bot API token](https://core.telegram.org/bots/api#authorizing-your-bot), etc:
    ```
    [telegrambot]
    # Your Telegram Bot API token
    token = 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

    [proxy]
    # address = www.example.com:8080

    [message_plugins]
    1 = plugins/*.py
    # 2 = other/plugins/foo.py

    [env]
    # Set any additional environment variables your plugins may need
    BOT_NAME = txTelegramBot
    # FOO = bar
    ```

* Write a plugin using the following template and add it in the \[message_plugins\] section above:
    ```
    from twisted.internet import defer
    from TelegramBotAPI.types import sendMessage
    from TelegramBot.plugin.message import MessagePlugin


    class MyPlugin(MessagePlugin):
        def startPlugin(self):
            pass

        def stopPlugin(self):
            pass

        @defer.inlineCallbacks
        def on_message(self, msg):
            m = sendMessage()
            m.chat_id = msg.chat.id
            m.text = 'You said: %s' % msg.text
            rsp = yield self.send_message(m)
            defer.returnValue(True)
    ```

* Run the bot:
    ```
    $ twistd -n telegrambot -c config.ini
    ```
