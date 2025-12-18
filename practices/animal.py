"""Heritage"""

class Animal:
    def __init__(self, name: str, habitat: str, diet: str) -> None:
        self.name = name
        self.habitat = habitat
        self.diet = diet

    def moviment(self) -> None:
        print(f'{self.name} is moving')

class Dog(Animal):
    def bark(self) -> None:
        print(f'{self.name} is barking')

class Snake(Animal):
    def bite(self) -> None:
        print(f'{self.name} is biting')

    def moviment(self) -> None:
        print(f'{self.name} is crawling')


if __name__ == '__main__':
    dog = Dog('Scott','City','carnivore')
    naguini = Snake('Naguini','Forest','carnivore')

    print(dog.name,dog.habitat,dog.diet)
    dog.moviment()
    dog.bark()
    print('------------------------------------------')
    print(naguini.name,naguini.habitat,naguini.diet)
    naguini.moviment()
    naguini.bite()

