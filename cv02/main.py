from random import random

def get_color():
    value = random * 100
    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1

def start_game():
    user_bilance = 1_000
    print("Welcome to casino Royal")
    bet = int(input("Select your bet ():"))
    print("Select color:")
    print("\t\t0 - Red")
    print("\t\t1 - White")
    print("\t\t2 - Green")
    print("\t\t9 - Leave game")
    selection = int(input("Select: "))
    print()


if __name__ == "__main__":
    start_game()
    total_count = 0
    color = 0
    for _ in range(1_000):
        if get_color() == 2:
            color = color + 1
    total(color / total_count * 100)