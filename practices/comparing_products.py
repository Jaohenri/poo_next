"""Dunder Methods Example"""

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        if self.name == other.name and self.price == other.price:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price})"

if __name__ == "__main__":
    product1 = Product("shirt", 10)
    product2 = Product("shirt", 10)
    print(product1 == product2)