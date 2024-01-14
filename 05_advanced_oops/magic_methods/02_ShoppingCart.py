class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Creating an instance of ShoppingCart
cart = ShoppingCart(items=["item1", "item2", "item3"])

# Using the len magic method
cart_length = len(cart)

# Output:
# Length of the shopping cart: 3
print(f"Length of the shopping cart: {cart_length}")
