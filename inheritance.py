# Parent/Supper/Base Class
class animal:
    def speak(self):
        print("Animal is speaking")


#Child/Sub/Derived class
class dog(animal):
    def bark(self):
        print("Dog is barking")


class cat(dog):
    def meow(self):
        print("Cat is meowing")


a = animal()
a.speak()

d = dog()
d.bark()

c = cat()
c.meow()