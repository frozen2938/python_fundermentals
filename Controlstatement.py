temperature = float(input("Enter temperature: "))

if temperature > 25 :
    print("It is too hot")

else :
    print("It is too cold")

# A program that returns the smallest number
first = input("Enter first number: ")
second = input("Enter second number: ")
third = input("Enter third number: ")


if first < second and first < third :
    print(first, "is the smallest number")
elif second < first and second < third :
    print(second, "is the smallest number")
else :
    print(third, "is the smallest number")

number = 0
if number == 0:
    print("number is neutral")
elif number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
