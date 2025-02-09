#Built-In Functions/Standard Library functions

y = max(67, 43, 89, 90, 23)
print("The maximum value is", y)

x = min(15, 3, 40, 90, 20, 73)
print("The minimum value is", x)

#User Defined Functions
def name():
    print("Geoffrey")

name()# Calling a function

def multiply():
    x = 10
    y = 2
    print(x * y)

multiply()



# Parameter/Valuable an Arguement/Value
def add(a, b):
    print(a + b)

add(1, 4)
add(6, 7)

def employee(name, gender, position, salary, age):
    print(name, gender, position, salary, age)

employee("Mark", "Male", "CEO", 560000, 67)
employee("John", "Male", "Managing director", 460000, 57)
employee("Mary", "female", "HR", 400000, 35)
employee("Mary", "female", "HR", 400000, 35)
employee("Mary", "female", "HR", 400000, 35)


#A program that displays details of five students
#Use a user defined function with the help of parameter and arguement
#Fullname, age, course, gender

def student(fullname, age, course, gender):
    print(fullname, age, course, gender)


student("John Mwaura", 17, "MIT", "Male")
student("Geoffrey Mwaniki", 18, "MIT", "Male")
student("Groly Makena", 16, "Cyber Security", "Female")
student("Shalon Mwendwa", 20, "Computer Packages", "Female")
student("Fabian Mwirigi", 19, "Cyber Security", "Male")
