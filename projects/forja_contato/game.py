class Entity:
    def __init__(self, name):
        self.name = name
        self.active = True

    def set_active(self,active):
        self.active = active

    def is_active(self):
        return self.active      

class Game(Entity):

    def __init__(self, name, synopsis, genre, platform,engine, status):
        super().__init__(name)
        self.synopsis = synopsis
        self.genre = genre
        self.platform = platform
        self.engine = engine
        self.status = status

class Person(Entity):
    def __init__(self, name, email, address, position):
        super().__init__(name)
        self.email = email
        self.address = address
        self.position = position



   