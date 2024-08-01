import time
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def display_fruit_list():
    print("Fruit List:")
    print("1. Banana - $20")
    print("2. Apple - $30")
    print("3. Orange - $40")

def buy_fruits():
    budget = 50
    user_budget = budget
    cart = []

    while True:
        display_fruit_list()
        print(f"\nYour budget: ${user_budget}")

        choice = input("Enter the number of the fruit you want to buy (0 to exit): ")

        if choice == '0':
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > 3:
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        selected_fruit = None
        if choice == 1:
            selected_fruit = Fruit("Banana", 20)
        elif choice == 2:
            selected_fruit = Fruit("Apple", 30)
        elif choice == 3:
            selected_fruit = Fruit("Orange", 40)

        if selected_fruit.price > user_budget:
            print("Not enough budget to buy this fruit.")
        else: # /check budget limit
            cart.append(selected_fruit)
            user_budget -= selected_fruit.price
            print(f"You've added {selected_fruit.name} to your cart. Remaining budget: ${user_budget}")

            if user_budget == 0:
                print("You've reached your budget limit. Exiting the prompt.")
                break

    print("\nYour Cart:")
    for item in cart:
        print(f"{item.name} - ${item.price}")

if __name__ == "__main__":
    buy_fruits()
