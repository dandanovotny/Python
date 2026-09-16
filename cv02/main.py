from random import random

def get_color():
    value = random() * 100
    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1

def start_game():
    user_bilance = 1_000
    print("Welcome to casino Royal")
    while True:
        bet = int(input(f"Select your bet ({user_bilance}eur):"))
        print("Select color:")
        print("\t\t0 - Red")
        print("\t\t1 - White")
        print("\t\t2 - Green")
        print("\t\t9 - Leave game")

        selection = int(input("Select: "))

        if selection == 9:
            return

        if selection == get_color():
                user_bilance = user_bilance + bet * 2
                print("You won!")
        else:
            print("You lost {bet}eur")
            user_bilance = user_bilance - bet


if __name__ == "__main__":
        start_game()