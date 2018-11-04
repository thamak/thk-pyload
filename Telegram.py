# -*- coding: utf-8 -*-

import pycurl
from module.network.RequestFactory import getRequest as get_request

from ..internal.Notifier import Notifier


class Telegram(Notifier):
    __name__ = "Telegram"
    __type__ = "hook"
    __version__ = "0.01"
    __status__ = "testing"

    __config__ = [("activated", "bool", "Activated", False),
                  ("botapikey", "str", "Bot Token Key", ""),
                  ("chatid", "str", "Chat ID", ""),
                  ("captcha", "bool", "Notify captcha request", True),
                  ("reconnection", "bool", "Notify reconnection request", False),
                  ("downloadfinished", "bool", "Notify download finished", True),
                  ("downloadfailed", "bool", "Notify download failed", True),
                  ("packagefinished", "bool", "Notify package finished", True),
                  ("packagefailed", "bool", "Notify package failed", True),
                  ("update", "bool", "Notify pyLoad update", False),
                  ("exit", "bool", "Notify pyLoad shutdown/restart", False),
                  ("sendinterval", "int",                  "Interval in seconds between notifications", 1),
                  ("sendpermin", "int", "Max notifications per minute", 60),
                  ("ignoreclient", "bool", "Send notifications if client is connected", True)]

    __description__ = """Send push notifications to your phone using Telegram"""
    __license__ = "GPLv3"
    __authors__ = [("Thamak", "")]

    def get_key(self):
        return self.config.get('tokenkey')

    def get_chatid(self):
        return self.config.get('chatid')

    def send(self, event, msg, key):
        req = get_request()
        #url='https://api.telegram.org/bot{0}/sendMessage'.format(str(key))

        self.load("https://api.telegram.org/bot314995357:AAHpYBup9B6Ckd8alpMTY4Cb08YyqA21oxM/sendMessage",
                post={'chat_id': '322102500',
                      'text': 'kikoo'},
                req=req)