"""Dunder Methods"""

class Shopping_cart:
    def __init__(self):
        self.cart = {}

    def __setitem__(self, product, quantity):
        if quantity <= 0:
            print("Quantity cannot be 0 or less")
        else:
            self.cart[product] = quantity

    def __getitem__(self, product):
        return self.cart.get(product, "Not found")
    
if __name__ == "__main__":
    cart = Shopping_cart()
    cart["shirt"] = 100
    print(cart["shirt"])
        