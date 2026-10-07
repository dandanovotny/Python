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
    for i in range(N):
        print(f"{i + 1}")
        if N % 2 == 0:
            sum += N
    print(sum)

def backwards():
    N = int(input("Zadejte cislo: "))
    for i in range(N):
        print(f"{N-i}")


if __name__ == "__main__":
    backwards()