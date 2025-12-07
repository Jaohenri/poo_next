class Human:
    life = 100
    def __init__(self, name, race, gender, char_class):
        self.name = name
        self.race = race
        self.gender = gender
        self.char_class = char_class

        if self.char_class == "Warrior":
            self.strength = 15
            self.intelligence = 5
            self.agility = 10
        elif self.char_class == "Mage":
            self.strength = 5
            self.intelligence = 15
            self.agility = 10
        elif self.char_class == "Archer":
            self.strength = 10
            self.intelligence = 10
            self.agility = 15
        else:
            self.strength = 10
            self.intelligence = 10
            self.agility = 10

class monster:
    life = 100
    def __init__(self, name, monster_type):
        self.name = name
        self.monster_type = monster_type

        if self.monster_type == "Goblin":
            self.strength = 8
            self.intelligence = 5
            self.agility = 12
        elif self.monster_type == "Orc":
            self.strength = 15
            self.intelligence = 3
            self.agility = 7
        elif self.monster_type == "Troll":
            self.strength = 12
            self.intelligence = 4
            self.agility = 8
        else:
            self.strength = 10
            self.intelligence = 10
            self.agility = 10

gandalf = Human("Gandalf","Human","Male","Mage")
legolas = Human("line","Human","Female","Archer")
goblin = monster("Gobby","Goblin")
orc = monster("Orcy","Orc")

print(gandalf.name, gandalf.race, gandalf.gender, gandalf.char_class, 
      gandalf.life, gandalf.strength, gandalf.intelligence, gandalf.agility)
print(legolas.name, legolas.race, legolas.gender, legolas.char_class, 
      legolas.life, legolas.strength, legolas.intelligence, legolas.agility)
print(goblin.name, goblin.monster_type, 
      goblin.life, goblin.strength, goblin.intelligence, goblin.agility)
print(orc.name, orc.monster_type, 
      orc.life, orc.strength, orc.intelligence, orc.agility)