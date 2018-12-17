from abc import ABC, abstractmethod
class WriteFile(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def write(self):
        pass

class LogFile(WriteFile):

    def write(self):
        pass

class DelimFile(WriteFile):

    def write(self):

        pass
