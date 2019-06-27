print("  _    _  ")
print(" | |  | |  ")
print(" | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print(" |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print(" | |  | | (_| | | | | (_| | | | | | | (_| | | | |")
print(" |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                      __/ |                      ")
print("                     |___/                       ")

print(" _________     ")
print("|         |    ")
print("|         0    ")
print("|        /|\  ")
print("|        / \  ")
print("|              ")
print("|              ")

i = 0

Player_word = input("Type a word for the other player to guess! Remember to keep it secret!")
low_word = Player_word.lower()


print("_ " * len(Player_word))

print("The word you have to guess is")
print(len(Player_word))
print("Letters long!")
print("Goodluck!")

while i < 6:
    ask1 = input("Guess a letter!")
    print(ask1)

    for each index in range(len(low_word)):
        print("Yay!")

    else:
        print("It's not in the word!")
        i += 1
        print("You have %d tries left!" %(6-i))
