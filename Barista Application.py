import time
import random

print("Hello and welcome to the cafe shop's job application!")
time.sleep(4)
def get_name():
    while True:
     name = input("What is your name? ")
     if not any(char.isdigit() for char in name):
        return name
    else:
        print("Names does not contain numbers")

name = get_name()
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid age.")

forbidden_name = ["John", "Jalil", "Jack"]

if name in forbidden_name:
    print("You are not welcomed here!")
    exit()
elif age <= 18:
    print("You are too young to work here, sorry.")
else:
    print("Congratulations, " + name + "! You have been promoted as an entry-level barista!")
    time.sleep(3)
    if age <= 30:
        print("Woah, you are the youngest employee here as you are " + str(age) + " years old!")

salary = random.uniform(30.000, 60.000)
cut = "{:.3f}".format(salary)
time.sleep(2)
print("Your starting salary is: " + str(cut) + " DZD!")
# this is the basics of python all in 38 lines :)