import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Initialize a variable to keep track of the number of guesses
num_guesses = 0

while True:
    try:
        # Ask the user for their guess
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Compare the user's guess with the target number
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
