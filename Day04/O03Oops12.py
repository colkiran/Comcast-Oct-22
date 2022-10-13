
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'angularJS', 'reactJS']

    def __str__(self):
        return self.__name + " - " + ", ".join(self.tech)

emp1 = Employee("Mike")
print(emp1)

print("-" * 40)

# print(emp1.__name)

print(emp1.__dict__)

print(emp1._Employee__name)
emp1._Employee__name = "Louis"

print(emp1)

print(emp1.__dict__)
