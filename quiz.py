answer_list = ["Xiaomi", "Tesla", "Python", "Ilon Mask"]
age = int(input("How old are you? "))
print(age)

if age <= 12:
    print("You are to young for this quest")
else:
    question = input("Who is the creator of AI GTP-3?\nTesla, Python, Ilon Mask, Xiaomi")
    print(question)

    if question == answer_list[1] or answer_list[3]:
        print("This is damn right!")
    else:
        print("Go learn some history!")