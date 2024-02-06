import threading


class UserInputReader(threading.Thread):
    def __init__(self):
        super(UserInputReader, self).__init__()
        self.result = None

    def run(self):
        self.result = input()
