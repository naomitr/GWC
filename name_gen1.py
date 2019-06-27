from random import *
First_Name = ["Alligator", "Elephant", "Dik-Dik", "Frog", "Pig", "Spade", "Bear", "Snake", "Sheep", "Bat", "Wood"]
Last_Name = ["Dropper", "Scratcher", "Presser", "Mimer", "Crusher", "Exploder", "Shifter", "Molder", "Engraver", "Smasher", "Scrubber"]

i = 0
while i < 5:
    aRandomIndex0 = randint(0, len(First_Name)-1)
    aRandomIndex1 = randint(0, len(Last_Name)-1)
    print((First_Name [aRandomIndex0]) + " " + (Last_Name[aRandomIndex1]))
    print(i)
    i += 1
