import math
# 2.5
def year(number):
    return (number % 400 == 0) or ((number % 4 == 0) and (number % 100 != 0))
# 1.5
def mean():
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    x3 = int(input("x3: "))

    print(f"Result is: {x1+x2+x3/3}")
# 3.1
def vypis():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{i + 1}")
# 3.4
def even_sum():
    N = int(input("Zadej cislo: "))
    sum = 0
    for i in range(N + 1):
        if i % 2 == 0:
            sum += i
    print(f"sum: {sum}")
# 3.2
def backwards():
    N = int(input("Zadejte cislo: "))
    for i in range(N):
        print(f"{N-i}")
# 3.6
def nasobilka():
    N = int(input("Zadejte cislo: "))
    for i in range(1, 11):
        print(f"{N*i}")
# 7.1
def minimum():
    N = int(input("Zadejte cislo: "))
    min = N
    while N != -1:
        if min > N:
            min = N
        N = int(input("Zadejte cislo: "))
    print(f"Minimum je: {min}")
# 3.3
def summ():
    N = int(input("Zadej cislo: "))
    print(f"{(N*(N+1)) / 2}")
# 4.1
def factorial():
    result = 1
    N = int(input("Zadej cislo: "))
    for i in range(N + 1):
        result = result * i
    print(f"Fakorial je: {result}")
#5.1
def factorial_comb(N):
    result = 1
    for i in range(1, N + 1):
        result = result * i
    return result
# 5.1
def combination_num():
    N = int(input("Zadej cislo: "))
    K = int(input("Zadej cislo: "))
    print(factorial_comb(N) / (factorial_comb(K) * (factorial_comb(N - K))))
# 4.2
def factorial_3(N):
    if N <= 1:
        return 1
    return N * factorial_3(N - 1)
# 2.1
def even_odd():
    N = int(input("Zadej cislo: "))
    if N % 2 == 0:
        print("Cislo je sude ")
    else:
        print("Cislo je liche ")
# 15.1
def obdelnik():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    O = 2*(a + b)
    S = a * b
    print(f"obvod: {O}")
    print(f"obsah: {S}")
# 15.2
def kruh():
    r = float(input("Zadejte polomer kruhu: "))
    o = 2 * math.pi * r
    S = math.pi * (r ** 2)
    print(f"obvod kruhu je {o}")
    print(f"obsah kruhu je {S}")
# 7.2
def highest_num():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    c = int(input("Zadejte cislo: "))

    highest = max(a,b,c)
    print(f"Nejvyssi cislo je: {highest}")
# 15.3
def pyth():
    a = int(input("Zadejte cislo: "))
    b = int(input("Zadejte cislo: "))
    c = ((a ** 2) + (b ** 2)) ** 0.5
    print(f"Toto je velikost c: {c}")
#1
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

# 7.3
def prumer_N():
    N = int(input("Zadej kolik chces zadat cisel: "))
    numbers = []
    for i in range(N):
        number = int(input(f"Zadej {i+1}. cislo: "))
        numbers.append(number)

    print(sum(numbers) / len(numbers))

# 7.5 / 7.6
def pocet():
    N = int(input("Zadejte cele kladne cislo: "))
    lst = []
    while N != 0:
        lst.append(N % 10)
        N = N // 10
    print(len(lst)) #sum/len

# 9.1
def NSD():
    a = int(input("Zadejte cislo a: "))
    b = int(input("Zadejte cislo b: "))
    while b != 0:
        a, b = b, a % b
        print(f"{a}")

def NSD_NSN(a,b):
    while b != 0:
        a, b = b, a % b

# 9.2
def NSN():
    a = int(input("Zadejte cislo a: "))
    b = int(input("Zadejte cislo b: "))
    print(+(a * b) / NSD_NSN(a,b))

# 11.1
def length():
    text = input("Zadejte text: ")
    print(len(text))

# 11.3
def palindrom():
    txt = input("Zadejte text: ")
    pal = txt[::-1]
    if pal == txt:
        print("Zadane slovo je palindrom")
    else:
        print("Zadane slovo neni palindrom")

# 11.4
def samo():
    txt = input("Zadejte text: ")
    lst = ["a", "e", "i", "o", "u"]
    for c in lst:
        counter = 0
        for h in txt:
            if c.capitalize() == h.capitalize():
                counter += 1
        print(f"V textu se nachazi {c} -> {counter}")

# 11.5
def znaky():
    text = input("Zadej text")
    dct = {}
    for i in text:
        if i in dct.keys():
            counter = dct[i] + 1
            dct[i] = counter
        else:
            dct[i] = i
    print(dct)

# 12.1
def list_sum():
    N = input("Zadejte cisla: ")
    number = [int(x) for x in N.split()]
    print(sum(number))

# 12.3
def seznam():
    N = input("Zadejte cisla: ")
    number = []
    for i in N.split():
        number.append(int(i))
    print(number[::-1])

# 12.4
def dupe():
    N = input("Zadejte cisla: ")
    cislo = []
    for i in N.split():
        a = int(i)
        if a not in cislo:
            cislo.append(a)
    print(cislo)

# 12.2
def maxmim():
    N = input("Zadejte cisla: ")
    numbers = []
    min = float("inf")
    max = float("-inf")
    for i in N.split():
        a = int(i)
        if a > max:
            max = a
        if a < min:
            min = a
    print(f"max {max} min {min}")

# 13.1
def linear():
    x = int(input("Zadejte vice cisel: "))
    lst = []
    for _ in range(x):
        i = int(input("Zadej cislo: "))
        lst.append(i)
    p = int(input("Zadej cislo, ktere hledas: "))
    for index, num in enumerate(lst):
        if num == p:
            print(f"Cislo se nachazi v seznamu na indexu {index}")
            return
    print("Cislo se nenachazi v seznamu")

def binarysearch():
    search = 6
    lst = [6,1,2,3,4,5]
    lst.sort()
    print(lst)
    left = 0
    right = len(lst) - 1
    middle = (left + right) // 2
    while right - left != 1:
        middle = (left + right) // 2
        if lst[middle] == search:
            print("Nalezeno")
            return 1
        if lst[middle] > search:
            right = middle
        if lst[middle] < search:
            left = middle
    if lst[0] == search or lst[-1] == search:
        print("Nalezeno")
        return 1
    print("Nenalezeno")
    

if __name__ == "__main__":
    linear()
