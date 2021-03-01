class Helicopter:
    def __init__(self, max_lifting_weight = 0, name = 'no', max_height = 0):
        self.max_lifting_weight = max_lifting_weight
        self.name = name
        self.max_height = max_height


    def __str__(self):
        return "Maximum lifting weight: " + str(self.max_lifting_weight) + \
               ",  Name: " + self.name + \
               ",  Maximum height:" + str(self.max_height)
