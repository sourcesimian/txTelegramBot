
class MessagePlugin(object):
    priority = 100

    def __init__(self, cb_send_method):
        self.__cb_send_method = cb_send_method

    def startPlugin(self):
        pass

    def stopPlugin(self):
        pass

    def on_message(self, msg):
        pass

    def send_method(self, method):
        return self.__cb_send_method(method)
