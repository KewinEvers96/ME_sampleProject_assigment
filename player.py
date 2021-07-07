
class Player:

    def __init__(self, id, name, height):
        self.id = name
        self.name = name
        self.height = height
    
    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name