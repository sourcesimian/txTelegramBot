import os
from configparser import ConfigParser

from twisted.application import service
from twisted.application.service import IServiceMaker
from twisted.plugin import IPlugin
from twisted.python import usage
from zope.interface import implementer

from TelegramBot.service.bot import BotService
from TelegramBotAPI.client.twistedclient import TwistedClient


class Options(usage.Options):
    optParameters = [
        ['config', 'c', None, 'Configuration file.'],
    ]


@implementer(IServiceMaker, IPlugin)
class ServiceMaker(object):
    tapname = "telegrambot"
    description = "Telegram Bot"
    options = Options

    def makeService(self, options):
        if options['config'] is None:
            print('Config file not specified')
            exit(1)
        config = ConfigParser()
        config.optionxform = str
        config.read([options['config']])

        token = config['telegrambot']['token']

        proxy = config['proxy'].get('address', None)
        if proxy:
            os.environ['http_proxy'] = 'http://%s' % proxy
            os.environ['https_proxy'] = 'https://%s' % proxy

        msg_plugins = [v for v in config['message_plugins'].values()]

        for key, value in config['env'].items():
            os.environ[key] = value

        multi = service.MultiService()

        bot = BotService(plugin_filespec=msg_plugins)
        bot.setServiceParent(multi)

        client = TwistedClient(token, bot.on_update, proxy=proxy)
        client.setServiceParent(multi)

        return multi


serviceMaker = ServiceMaker()
