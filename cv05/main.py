def year(number):
    return (number % 400 == 0) or ((number % 4 == 0) and (number % 100 != 0))

def mean():
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    x3 = int(input("x3: "))

    print(f"Result is: {x1+x2+x3/3}")

def vypis():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{i + 1}")

def even_sum():
    N = int(input("Zadej cislo: "))
    sum = 0
    for i in range(N + 1):
        if i % 2 == 0:
            sum += i
    print(f"sum: {sum}")

def backwards():
    N = int(input("Zadejte cislo: "))
    for i in range(N):
        print(f"{N-i}")

def nasobilka():
    N = int(input("Zadejte cislo: "))
    for i in range(1, 11):
        print(f"{N*i}")

def minimum():
    N = int(input("Zadejte cislo: "))
    min = N
    while N != -1:
        if min > N:
            min = N
        N = int(input("Zadejte cislo: "))
    print(f"Minimum je: {min}")

def sum():
    N = int(input("Zadej cislo: "))
    print(f"{(N*(N+1)) / 2}")


if __name__ == "__main__":
    even_sum()