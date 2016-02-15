from twisted.internet import defer, task
from twisted.python import log

from TelegramBotAPI.types import sendMessage, sendPhoto
from TelegramBotAPI.types import Message

from TelegramBot.plugin.message import MessagePlugin

from datetime import datetime


class Timer(MessagePlugin):
    priority = 10
    _chat_id = None

    def startPlugin(self):
        self._loop = task.LoopingCall(self.on_tick)

    def stopPlugin(self):
        if self._loop.running:
            self._loop.stop()

    @defer.inlineCallbacks
    def on_tick(self):
        m = sendMessage()
        m.chat_id = self._chat_id
        m.text = "Time now is: %s" % datetime.now()
        yield self.send_method(m)

    @defer.inlineCallbacks
    def on_message(self, msg):
        if not hasattr(msg, 'text'):
            defer.returnValue(False)

        if isinstance(msg, Message):
            if msg.text.lower() == 'timer start':
                self._loop.start(interval=5, now=False)
                m = sendMessage()
                m.chat_id = msg.chat.id
                self._chat_id = msg.chat.id
                m.text = 'Timer started'
                yield self.send_method(m)
                defer.returnValue(True)
            if msg.text.lower() == 'timer stop':
                self._loop.stop()
                m = sendMessage()
                m.chat_id = msg.chat.id
                self._chat_id = None
                m.text = 'Timer stopped'
                yield self.send_method(m)
                defer.returnValue(True)

