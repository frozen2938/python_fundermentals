courses = ["MIT", "Cyber security", "Data Science"]
print(courses)

#Accessing an element
print(courses[2])

#looping through an array
for a in courses:
    print("Choose", a)

#adding an element into an array
courses.append("Laravel")
print(courses)

#deleting an element from an array
courses.remove("Cyber security")
print(courses)