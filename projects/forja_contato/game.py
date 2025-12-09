class Game:
    def __init__ (self,name, synopsis, genre, platform,engine, status):
        self.name = name
        self.synopsis = synopsis
        self.genre = genre
        self.platform = platform
        self.engine = engine
        self.status = status
        self.active = True

    def set_active(self,active):
        self.active = active

    def is_active(self):
        return self.active