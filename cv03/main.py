# aritmicke op.

## and or
# prirazovaci
## =, +=, -=, *=, /=
# bitovy
## &, |, ^, <<, >>, ~

# A = 0b10100111
# B = 0b10011010
 
# A & B = 0b10000010
# A | B = 0b10111111
# A ^ B = 0b00111101
# ~A = 0b01011000
# A << 4 = 0b01110000
# B >> 4 = 0b00001001

## Nactete INT ze vstupu a naformatujte ho na hh:mm:ss

## 360 -> 00:06:00

def time ():
    if __name__ == "__main__":
        str_time = input("Zadej cas v s:")
        time = int(str_time)
        hour = time // 3600
        minut = (time % 3600) // 60
        second = (time % 3600) % 60
        print(f"{hour}:{minut}:{second}")

if __name__ == "__main__":
    #Vytvorte automat, který vam rozmeni castku X na:
    # 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1
    value = int(input("Zadej castku: "))
    money = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for item in money:
        x = value // item
        value = value - (x * item)
        print(x)
"""
    x_2000 = value // 2000
    value = value - (x_2000 * 2000)
    x_1000 = value // 1000
    value = value - (x_1000 * 1000)
    x_500 = value // 500
    value = value - (x_500 * 500)
    x_200 = value // 200
    value = value - (x_200 * 200)
    x_100 = value // 100
    value = value - (x_100 * 100)
    x_50 = value // 50
    value = value - (x_50 * 50)
    x_20 = value // 20
    value = value - (x_20 * 20)
    x_10 = value // 10
    value = value - (x_10 * 10)
    x_5 = value // 5
    value = value - (x_5 * 5)
    x_2 = value // 2
    value = value - (x_2 * 2)
    x_1 = value // 1
    value = value - (x_1 * 1)
    """