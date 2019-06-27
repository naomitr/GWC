my_name = "EveBot-3000"
input_name = input("Can you guess what my name is?")
if input_name == my_name:
  print("You guessed correctly! My name is EveBot-3000!")
else:
  print("Sorry, you got it wrong! Try again!")
input_hint = input ("Do you want a hint?")
if input_hint == "Yes":
    print("My name is from a movie, well, the first part of it is...")
