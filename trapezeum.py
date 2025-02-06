#A program to return the area of a trapezeum
# A = 1/2 (a+b) h

toplength = int(input("Enter the top length:"))
bottomlength = int(input("Enter the bottom length:"))
height = int(input("Enter the height:"))

area = (toplength + bottomlength) / 2 * height
print("The area is", area)
