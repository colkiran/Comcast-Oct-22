
class Employee:

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = Employee("David", 45000, 29)
emp2 = Employee("Smith", 15000, 23)

print(f"Add :{emp1 + emp2}")
print(f"Sub :{emp1 - emp2}")
print(f"Mul :{emp1 * emp2}")
print(f"Div :{emp1 / emp2}")
print(f"FlrDiv :{emp1 // emp2}")
