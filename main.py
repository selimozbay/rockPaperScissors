# Rock Paper Scissors

import random

game_on = True
available_choices = ("1", "r", "rock", "2", "p", "paper", "3", "s", "scissors")

print("ROCK PAPER SCISSORS")

while game_on:

    user_choice = input("1 (R)ock\n2 (P)APER\n3 (S)CISSORS\n").strip().lower()

    if user_choice in available_choices:

        pc_choice = random.randint(1, 3)

        if user_choice in (available_choices[0], available_choices[1], available_choices[2]):
            user_choice = 1

        elif user_choice in (available_choices[3], available_choices[4], available_choices[5]):
            user_choice = 2

        else:
            user_choice = 3

        if pc_choice == user_choice:
            print("DRAW")

        elif ((user_choice == 1 and pc_choice == 3) or
              (user_choice == 2 and pc_choice == 1) or
              user_choice == 3 and pc_choice == 2):
            print("WIN")

        else:
            print("LOSE")

    else:
        print("\nIncorrect Choice\n")
