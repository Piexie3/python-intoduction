import random



guess = "food"
##getting the number of characters in the string
numchar = len(guess)
randnumber = random.randint(0,numchar-1)
givenhints = []
print("Welcome to the word guessing game!")
choice = input("What is your guess? " )
if choice == numchar:
       print("You won")
else:
    print("You lost try next attempt")
    givenhints.append(randnumber)
    
    choice = input("What is your guess? ")
    

 
print(f"Your hint is:"+" _ "*numchar)
