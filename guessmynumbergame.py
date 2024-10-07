import random

number = str(random.randint(1, 10))

print("Let's play a game!")
print("I'm thinking of a number between 1 and 10.")
choice = input("What number am I thinking of?: ")

if number == choice:
    print("Hurray! you won")
else:
    print("You are a looser!")
    print("\n")
    print(f"I was thinking of number " + number)