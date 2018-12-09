class MaxSizeList():
    #my_list = []
    #max_size = 0
    def __init__(self, max_size):
        self.my_list = []
        self.max_size = max_size
    
    def get_list(self):
        return self.my_list
    

    def push(self, element):
        #print(self.my_list)
        self.my_list.append(element)
        #print(self.my_list)
        if len(self.my_list) > self.max_size:
            #self.my_list.pop()
            self.my_list.pop(0)




