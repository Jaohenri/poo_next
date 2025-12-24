"""Heritage example"""

class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
class Employee(People):
    def __init__(self, name: str, age: int, position) -> None:
        super().__init__(name, age)
        self.position = position

class Client(People):
    def __init__(self, name: str, age: int, gender: str, balance: float) -> None:
        super().__init__(name, age)
        self.gender = gender
        self.balance = balance

if __name__ == '__main__':

    bill = Employee('Bill', 45, 'Software engineer')
    jessyca = Client('Jessyca', 35, 'Female', 20000)

    print(bill.name,bill.age,bill.position)
    print(jessyca.name,jessyca.age,jessyca.gender,jessyca.balance)
        