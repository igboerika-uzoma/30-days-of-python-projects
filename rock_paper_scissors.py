import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "Scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked " + computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        continue

    if user_input == 'paper' and computer_pick == 'scissors':
        print("You won!")
        continue

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        continue

print("Goodbye")
