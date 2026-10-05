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
    for i in range(number):
        ans = number - init
        init += 1

    return ans

    
def fibbonachi_recursion(number):
    if number == 0 or number == 1:
        return 1
    
    return fibbonachi_recursion(number - 1) + fibbonachi_recursion(number - 2)
    
def combination_number():
    """
    Napiste funkci ktera vypocita kombinacni cislo
    """
def pascal_triangle():
    """
    010
    0110
    01210
    013310
    0146410

    Napiste funkci, ktera vypise X radek pascalova trojuhelniku
    """


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