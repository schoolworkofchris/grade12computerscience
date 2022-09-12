# Christian Moloci, Guessing Game

# Import Random Library for random number
import random

print("Guess my number!\n Pick a number between 1 and 9\nType 0 to exit")
x = True

while x == True:
    guess = int(input("My guess is: "))
    answer = random.randint(1, 9)

    if guess == 0:
        x = False
    elif guess == answer:
        print("Argh, you got me!")
    elif guess < answer:
        print("Too low, I win!")
    elif guess > answer:
        print("Too high, I win!")

    print("Type 0 to exit")
    print("\n")