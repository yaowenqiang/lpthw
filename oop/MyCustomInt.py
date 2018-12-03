class MyCustomInt(object):
    def __init__(self):
        self.val = 0

    
    def increment(self):
        self.val = self.val + 1


    def __repr__(self):
        return str(self.val)
