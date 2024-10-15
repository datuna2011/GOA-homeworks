def simple_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    elif operation == "":
        return num1 
print(simple_calculator(int(input("enter first num: ")), int(input("enter second num: ")), input("enter +, -, /, *: ")))







def find_max(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    elif num1 == num2:
        return num1, num2
print(find_max(int(input("enter num1: ")), int(input("enter num2: "))))