# Rock Paper Scissors

import random

R = "rock"
P = "paper"
S = "scissors"
D = "DRAW"
W = "WIN"
L = "LOSE"
IC = "Incorrect Choice"

available_choices = ("1", "r", R, "2", "p", P, "3", "s", S)

print(R.upper(), P.upper(), S.upper())

while True:

    user_choice = input("\n1 (R)ock\n2 (P)APER\n3 (S)CISSORS\n").strip().lower()

    if user_choice in available_choices:

        pc_choice = random.randint(1, 3)

        if pc_choice == 1:
            pc_choice_w = R.capitalize()

        elif pc_choice == 2:
            pc_choice_w = P.capitalize()

        else:
            pc_choice_w = S.capitalize()

        if user_choice in (available_choices[0], available_choices[1], available_choices[2]):
            user_choice = 1
            user_choice_w = R.capitalize()

        elif user_choice in (available_choices[3], available_choices[4], available_choices[5]):
            user_choice = 2
            user_choice_w = P.capitalize()

        else:
            user_choice = 3
            user_choice_w = S.capitalize()

        print("\n" + user_choice_w, "vs", pc_choice_w)
        if pc_choice == user_choice:
            print(D)

        elif (user_choice - pc_choice) in {1, -2}:
            print(W)

        else:
            print(L)

    else:
        print("\n" + IC + "\n")
