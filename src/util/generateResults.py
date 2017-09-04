import sys


class GenerateResults(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.res = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.res.write(message)
