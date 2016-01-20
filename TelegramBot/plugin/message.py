
class MessagePlugin(object):
    priority = 100

    def __init__(self, cb_send_message):
        self.__cb_send_message = cb_send_message

    def startPlugin(self):
        pass

    def stopPlugin(self):
        pass

    def on_message(self, msg):
        pass

    def send_message(self, msg):
        return self.__cb_send_message(msg)
