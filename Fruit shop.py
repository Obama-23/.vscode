class Item:
    def __init__(self, name: str, price: float, quantity: int):
        print(f"An instance has been created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
    
    def calculated_price(self):
        return self.price * self.quantity

# Create a list of items
items = [
    Item("Banana", 420, 2),
    Item("Apple", 600, 4),
    Item("Potato", 75, 5)
]

# Calculate and print the calculated price for each item
for item in items:
    print(f"{item.name}: {item.calculated_price()}")

# Perform actions on each item
for item in items:
    if item.price > 600:
        print(f"{item.name} is expensive! It costs {item.price} per kilo!")
    elif item.price < 600:
        print(f"{item.name} is cheap. It costs {item.price} per kilo!")
    else:
        print(f"{item.name} is reasonably priced. It costs {item.price} per kilo!")
        
# totally right!
# yes hehe 
