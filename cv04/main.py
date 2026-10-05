#list = [1,2,3,4,5,6, "Ahoj"]

#list.append(5)
#print(list[1]) # 2
#print(list[-1])
#del list[0]

#print(list)

#for i in range(10):
#    print(i)

if __name__ == "__main__":
    # Napiste program do ktereho uzivatel zacne vkladat cisla
    # kdyz zada -1, tak se zadavani zastavi a vzpise to max, min a mean
    lst = []
    number = None
    while number is None or number != -1:
        number = int(input("Zadej hodnotu: "))
        lst.append(number)
        

    print(f"Max value {max(lst)}")
    print(f"Min value {min(lst)}")
    print(f"Mean value {sum(lst) / len(lst)}")