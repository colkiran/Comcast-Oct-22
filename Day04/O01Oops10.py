
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'angularJS', 'reactJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Daniel", 35000)
print(emp1)
print("-" * 40)

print(len(emp1))

print("-" * 40)
print([t for t in emp1])            # list comprehension

