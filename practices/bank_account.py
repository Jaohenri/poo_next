"""Encapsulation example"""

class BankAccount:
    def __init__(self, owner: str, initial_balance: float) -> None:
        self.owner = owner
        self.__balance = initial_balance  #  Private atribute

    def deposit(self, value: float) -> None:
        if value > 0:
            self.__balance += value
        else:
            print('Invalid value to deposit')

    def withdraw(self, value:float) -> None:
        if 0 < value <= self.__balance:
            self.__balance -= value
        else:
            print('Not enough balance or invalid value')

    def show_balance(self) -> str:
        return f'Actual balance: R${self.__balance:.2f}'

if __name__ == '__main__':
    # Use
    account = BankAccount('João', 500)
    account.deposit(200)
    print(account.show_balance()) # Output: Actual balance: R$700.00
    #account.__balance = 1000        # Doesn't affect the real balance, because it's private.
    print(account.show_balance()) # Output: Actual balance: R$700.00
