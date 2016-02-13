import os

from twisted.internet import defer
from twisted.python import log

from TelegramBotAPI.types import sendMessage, sendPhoto

from TelegramBot.plugin.message import MessagePlugin


class Ping(MessagePlugin):

    def startPlugin(self):
        pass

    @defer.inlineCallbacks
    def on_message(self, msg):

        if msg.text:
            m = sendMessage()
            m.chat_id = msg.chat.id
            if msg.text == 'Hello':
                m.text = 'Hello my name is %s' % os.environ['BOT_NAME']
            else:
                m.text = '"%s"?' % msg.text
        elif msg.photo:
            m = sendPhoto()
            m.chat_id = msg.chat.id
            m.caption = "What a pong?"
            m.photo = msg.photo[0].file_id
        else:
            return

        log.msg("REPLY: %s" % m)
        rsp = yield self.send_method(m)
        log.msg("RSP: %s" % rsp)
        defer.returnValue(True)
