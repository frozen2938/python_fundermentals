#1. A program to check weather a year is a leap year or not
import re

n = 2024
x = 2025

#example one
if n % 4 == 0:
    print(n, "is a leap year")
else:
    print(n, "is not a leap year")

#example two
if x % 4 == 0:
    print(x, "is a leap year")
else:
    print(x, "is not a leap year")








#2. A program to check weather a letter is a consonant or a vowel

#reference
letter = "E"
mine = "z"

#example one
if re.match(r'[aeiouAEIOU]', letter):
    print("The Letter is a Vowel")
else:
    print("The Letter is a Consonant")

# example two
if re.match(r'[aeiouAEIOU]', mine):
     print("The Letter is a Vowel")
else:
     print("The Letter is a Consonant")

#second method for checking if a letter is a leap year or not
letter2 = "t"
if letter2 == 'a' or letter2 == 'e' or letter2 == 'i' or letter2 == 'o' or letter2 == 'u':
    print("The Letter is a Vowel")
else:
    print("The Letter is a Consonant")
