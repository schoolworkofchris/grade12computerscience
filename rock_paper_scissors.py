# Rock Paper Scissors By Christian Moloci
import random

# Welcome code
print("Welcome to rock, papaer, scissors!\nDo you have what it takes to beat a computer?")

# While loop to keep looping the program until the user wants to exit it
while True:
    # Get user's and computer's move
    user_move = str(input("Enter a choice: "))
    cpu_move = random.randint(1,3)

    # Condistions for user = rock
    if user_move.lower() == "rock" and cpu_move == 2:
        print("computer wins with paper")
    elif user_move.lower() == "rock" and cpu_move == 3:
        print("you win rock!")

    # Condistions for user = paper
    if user_move.lower() == "paper" and cpu_move == 1:
        print("you win with paper!")
    elif user_move.lower() == "paper" and cpu_move == 3:
        print("computer wins with scissors")

    # Conditions for user = scissors
    if user_move.lower() == "scissors" and cpu_move == 1:
        print("computer wins with rock")
    elif user_move.lower() == "scissors" and cpu_move == 2:
        print("you win scissors!")

    # Conditions for user = tie
    if user_move.lower() == "rock" and cpu_move == 1:
        print("It's a tie")
    elif user_move.lower() == "paper" and cpu_move == 2:
        print("It's a tie")
    elif user_move.lower() == "scissors" and cpu_move == 3:
        print("It's a tie")

    