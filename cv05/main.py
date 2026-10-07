import math

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

def factorial():
    result = 1
    N = int(input("Zadej cislo: "))
    for i in range(N + 1):
        result = result * i
    print(f"Fakorial je: {result}")

def factorial_comb(N):
    result = 1
    for i in range(1, N + 1):
        result = result * i
    return result

def combination_num():
    N = int(input("Zadej cislo: "))
    K = int(input("Zadej cislo: "))
    print(factorial_comb(N) / (factorial_comb(K) * (factorial_comb(N - K))))

def factorial_3(N):
    if N <= 1:
        return 1
    return N * factorial_3(N - 1)

def even_odd():
    N = int(input("Zadej cislo: "))
    if N % 2 == 0:
        print("Cislo je sude ")
    else:
        print("Cislo je liche ")

def obdelnik():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    O = 2*(a + b)
    S = a * b
    print(f"obvod: {O}")
    print(f"obsah: {S}")

def kruh():
    r = float(input("Zadejte polomer kruhu: "))
    o = 2 * math.pi * r
    S = math.pi * (r ** 2)
    print(f"obvod kruhu je {o}")
    print(f"obsah kruhu je {S}")

def highest_num():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    c = int(input("Zadejte cislo: "))

    highest = max(a,b,c)
    print(f"Nejvyssi cislo je: {highest}")

def pyth():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    c = ((a ** 2) + (b ** 2)) ** 0.5
    print(f"Toto je velikost c: {c}")

def huh():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    s = a + b
    print(f"Soucet je: {s}")
    r = a - b
    print(f"Rozdil je: {r}")
    p = a / b
    print(f"Podil je: {p}")
    q = a * b
    print(f"Soucin je: {q}")

    



if __name__ == "__main__":
    highest_num()