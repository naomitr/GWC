from random import *
i = 0
aRandomNumber = randiant(1,20)

while i < 2:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess)
        print (i)
        i += 1
