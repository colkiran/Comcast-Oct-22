
from functools import total_ordering

@total_ordering             # __eq__ and one more operator, will enable all comparison
class Employee:

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __eq__(self, other):            # works for __ne__ also
        return self.salary == other.salary

    def __gt__(self, other):            # works for __lt__ also
        return self.salary > other.salary


emp1 = Employee("Mike", 45000, 34)
print(emp1)
print("-" * 40)

emp2 = Employee("Tina", 55000, 32)
print(emp2)

print("-" * 40)
print(emp1 >= emp2)

print("-" * 40)

if emp1 > emp2:
    print("{}'s salary of {} is Greater Than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is NOT Greater Than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))


# if emp1 != emp2:
#     print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
# else:
#     print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
