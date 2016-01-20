import os

from unittest import TestCase

from TelegramBotAPI.client import BasicClient
from TelegramBotAPI.types.methods import getUpdates, sendMessage, sendPhoto

import env


class Methods(TestCase):

    def setUp(self):
        self._tgclient = BasicClient(env.token, env.proxy)

    def test_poll(self):
        m = getUpdates()
        m.timeout = 10
        m.limit = 100
        #m.offset = 585177182
        resp = self._tgclient.post(m)
        print(resp)

    def test_send(self):
        m = sendMessage()
        m.chat_id = env.uid
        m.text = "Hi there"
        resp = self._tgclient.post(m)
        print(resp)

    def test_send_photo(self):
        m = sendPhoto()
        m.chat_id = env.uid
        m.caption = "Pong to you!"
        m.photo = os.path.join(os.path.dirname(__file__), 'pong.png')

        resp = self._tgclient.post(m)
        print(resp)

