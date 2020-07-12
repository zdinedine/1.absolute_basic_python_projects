import random

def generator(password_lenght):
    x = 0
    list = []
    while x < password_lenght:
        list.append(random.choice(["1","2","3","4","5","6","7","8","9","0",'A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']))
        x += 1
    print("".join(list))



password_lenght = int(input("Enter the number representing the password's length"))
generator(password_lenght)