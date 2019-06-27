Women_In_Tech = ["Amanda Randles", "Dr. Aprille Joy Ericsson", "Cindy Alvarez", "Dorothy Vaughan","Jess Lee"]
print(*Women_In_Tech)
print(len(Women_In_Tech))
Girls_Who_Code = ["Adriana", "Julieta", "Kimberly", "Sydney", "Sharon", "Naomi"]
print(*Girls_Who_Code)
print(len(Girls_Who_Code))

for each in Girls_Who_Code:
    if each in Women_In_Tech:
        print(each + " is a Women of tech and a girl who codes!")
    else:
        print(each + " is a girls who codes")

for each in Women_In_Tech:
        print(each + " is a Woman in Tech!")

Women_In_Tech.insert(4,"Adriana")
print(*Women_In_Tech)

for each in Girls_Who_Code:
    if each in Girls_Who_Code in Women_In_Tech:
        print(each + " is a Women of tech and a girl who codes!")
    else:
        print(each + " is a girls who codes")
