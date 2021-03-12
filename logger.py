from datetime import datetime


class Logger(object):

    def __init__(self, name, debug=False):
        self.name = name
        self.level = debug

    def log(self, message):
        print("{} {}: {}".format(self.name, datetime.now().time(), message))

    def debug(self, message):
        if self.level:
            self.log(message)
