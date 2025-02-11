class employee:
    def __init__(self, name,position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def detail(self):
        print(self.name, "is the", self.position)

employee1 = employee("John", "CEO", 450000)
print(employee1.name, employee1.position, employee1.salary)

employee2 = employee("Jane", "Managing director", 300000)
print(employee2.name, employee2.position, employee2.salary)

employee3 = employee("Eunice", "HR", "150000")
print(employee3.name, employee3.position, employee3.salary)

employee4 = employee("Frozen", "Head of center", 450000)
print(employee4.name, employee4.position, employee4.salary)