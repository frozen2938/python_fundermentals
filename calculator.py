#+-*/
x = int(input("Enter first number: "))
operator = input("Enter operator: ")
y = int(input("Enter second number: "))

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    print(x / y)
else:
    print("Invalid operator")
