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
        if user_bilance == 0:
            print("You lost completely")
            return
        text = input(f"Select your bet ({user_bilance}€):")
        if not text.isnumeric():
            continue

        bet = int(text)
        if bet > user_bilance or bet <= 0:
            print("You dont have money!")
            return

        print("Select color:")
        print("\t\t0 - Red")
        print("\t\t1 - White")
        print("\t\t2 - Green")
        print("\t\t9 - Leave game")


        text2 = input("Select: ")
        if not text2.isnumeric():
            continue
        
        selection = int(text2)
        if selection == 9:
            return

        if selection == get_color():
                user_bilance = user_bilance + bet * 2
                print("You won!")
        else:
            print(f"You lost {bet}€")
            user_bilance = user_bilance - bet


if __name__ == "__main__":
        start_game()