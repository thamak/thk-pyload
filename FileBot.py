from module.plugins.Hook import Hook

class FileBot(Hook):
    __name__ = "FileBot"
    __type__ = "hook"
    __version__ = "0.1"
    __status__ = "testing"
    __description__ = "Do FileBot stuff"
    __license__ = "GPLv3"
    __authors__ = [("Thamak", "")]
    __config__ = [("activated", "bool", "Activated", True),
                  ("command", "str", "Custom command", "")]

    event_map = {
      "downloadFinished" : "doSomeWork",
      "coreReady": "initialize"
    }

    def initialize(self):
        print "Initialized."

    def doSomeWork(self, pyfile):
        print "This is equivalent to the above example." + self.config.get('command')

    def someMethod(self):
        print "The underlying event (allDownloadsFinished) for this method is not available through the base class"