
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

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


emp1 = Employee("George", 50000)
print(emp1)

print("-" * 40)

print([t for t in emp1])

print("-" * 40)

x = emp1[3]
print(f"x :{x}")

print("-" * 40)

emp1[3] = 'nodeJS'

print([t for t in emp1])
