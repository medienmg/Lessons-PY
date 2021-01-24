num1 = 0
num2 = 0

while True:
    num1 = input("Enter your thirst number: ")
    if not num1.isdigit():
        print("Error! Please use numbers instead the letters.")
        continue
    else:
        break

while True:
    num2 = input("Enter your second number: ")
    
    if not num2.isdigit():
        print("Error! Please use numbers instead the letters.")
        continue
    else:
        break

result = int(num1) + int(num2)
print("Your result: " + str(result))