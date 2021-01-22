try:
    a = int(input("enter num1 »"))
    b = int(input("enter num2: »"))
    sum = a + b
    print("результат: " + str(sum))
    input("")
    quit()

except:
    print("Ошибка.")
    input("")
    quit()