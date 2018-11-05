import os
from ..internal.Addon import Addon

class RunCommand(Addon):
    __name__ = "RunCommand"
    __type__ = "hook"
    __version__ = "0.1"
    __status__ = "testing"
    __description__ = "Do RunCommand stuff"
    __license__ = "GPLv3"
    __authors__ = [("Thamak", "")]
    __config__ = [("activated", "bool", "Activated", True),
                  ("command", "str", "Custom command", "")]

    def init(self):
        self.event_map = {'downloadFinished': "doSomeWork"}
        self.log_info("RunCommand Download Init")

    def doSomeWork(self, pyfile):
        cmd = self.config.get('command')
        self.log_info("Download Finished: " + cmd)
        self.log_info(os.popen(cmd).read())