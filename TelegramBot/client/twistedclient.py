from TelegramBotAPI.client.requestsclient import RequestsClient
from TelegramBotAPI.types.methods import getUpdates

from twisted.application import service
from twisted.internet import reactor, threads, defer
from twisted.python import log


class TwistedClient(service.Service):
    name = 'telegrambot_client'

    _limit = 10
    _timeout = 5
    _lock = None
    _poll = True
    _offset = None
    _poll_backoff = 0

    def __init__(self, token, on_update, proxy=None, debug=False):
        self._lock = defer.DeferredLock()
        self._token = token
        self._proxy = proxy
        self._debug = debug
        assert callable(on_update)
        self._on_update = on_update

    def startService(self):
        self._client = RequestsClient(self._token, proxy=self._proxy, debug=self._debug)
        reactor.callLater(0, self._poll_updates)

    def stopService(self):
        self._poll = False

    def send_method(self, m):
        d = self._lock.acquire()

        def do_send(_):
            return threads.deferToThread(self._send_thread, m)

        def do_release(value):
            self._lock.release()
            return value

        d.addCallback(do_send)
        d.addBoth(do_release)

        return d

    def _send_thread(self, m):
        resp = self._client.send_method(m)
        return resp

    @defer.inlineCallbacks
    def _poll_updates(self, _=None):
        while self._poll:
            yield threads.deferToThread(self._poll_updates_thread)
            if self._poll_backoff:
                d = defer.Deferred()
                reactor.callLater(self._poll_backoff, d.callback, None)
                log.msg('Backing off update poll for %s' % self._poll_backoff)
                self._poll_backoff = 0
                yield d

    def _poll_updates_thread(self):
        m = getUpdates()
        m.timeout = self._timeout
        m.limit = self._limit
        if self._offset is not None:
            m.offset = self._offset
        try:
            updates = self._client.send_method(m)
            reactor.callFromThread(self._handle_updates, updates)
        except Exception as e:
            reactor.callFromThread(self._handle_updates_error, e)
            # import traceback
            # log.msg(traceback.format_exc())

    @defer.inlineCallbacks
    def _handle_updates(self, updates):

        if updates:
            for update in updates:
                self._offset = update.update_id + 1
                try:
                    yield defer.maybeDeferred(self._on_update, update.message)
                except Exception as e:
                    # import traceback
                    # log.msg(traceback.format_exc())
                    log.msg(e)
                    pass

    def _handle_updates_error(self, e):
        raise e
        log.msg(e)
        self._poll_backoff = 5
