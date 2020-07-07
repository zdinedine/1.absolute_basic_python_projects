"""Write a programme where the computer randomly generates a number between 0 and 20.
The user needs to guess what the number is. If the user guesses wrong, tell them their 
guess is either too high, or too low. This will get you started with the random library 
if you haven't already used it."""

import random

n = random.randint(0, 20)
x = "string"
while x != n:
    l = input("Guess the number between 0 and 20!")
    x = int(l)
    if x > n: print("too high! Guess again!")
    elif x == n: print("You won!")
    else: print("Too low! Guess again!")



