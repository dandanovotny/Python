#list = [1,2,3,4,5,6, "Ahoj"]

#list.append(5)
#print(list[1]) # 2
#print(list[-1])
#del list[0]

#print(list)

#for i in range(10):
#    print(i)

def prime_number():
    """
    Napiste funkci, ktera zjisti jestli je na vstupu prime number
    """
    i = number ** 0.5
    while i > 1:
        if number % i == 0:
            return False
        i = i - 1
        return True

def factorial(number):
    """
    Napiste funkci, ktera vypocita hodnotu faktorialu
    """
    result = 1
    index = 1
    while index < number:
        result = result * index
        index += 1
    return result
           
def factorial_recursion(number):
    if number < 0:
        return 1
    return factorial_recursion(number - 1) * number

def fibbonachi():
    """ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    Napiste funkci, ktera vypocita X clen fibbonachiho posloupnosti
    """
    init = 1
    prev = 1
    
    prev = 1
    actual = 1
    if number < 2:
        return 1
    
    for _ in range(number):
        tmp = init + prev
        prev = init
        init = tmp
    return init
    
def fibbonachi_recursion(number):
    if number == 0 or number == 1:
        return 1
    
    return fibbonachi_recursion(number - 1) + fibbonachi_recursion(number - 2)
    
def combination_number(n, k):
    """
    Napiste funkci ktera vypocita kombinacni cislo
    """
    return factorial_recursion(n) / (factorial_recursion(n-k) * factorial_recursion(k))
def pascal_triangle(line_index):
    """
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
     1 5 10 10 5 1
    1 6 15 20 15 6 1
    Napiste funkci, ktera vypise X radek pascalova trojuhelniku
    """
    for item in range(line_index + 1):
        print(combination_number(line_index, item))

if __name__ == "__main__":
    # Napiste program do ktereho uzivatel zacne vkladat cisla
    # kdyz zada -1, tak se zadavani zastavi a vzpise to max, min a mean
    lst = []
    number = None
    while number is None or number != -1:
        number = int(input("Zadej hodnotu: "))
        if number == -1:
            break
        lst.append(number)
        

    print(f"Max value {max(lst)}")
    print(f"Min value {min(lst)}")
    print(f"Mean value {sum(lst) / len(lst)}")