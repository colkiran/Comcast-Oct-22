
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Hardik", 29)
# ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 28)
# ply2.get_details()

print("-" * 40)
print(str(ply1))                # __str__()
print("-" * 40)
print(str(ply2))

print("-" * 40)
print(ply1)                     # implicitly calls __str__
print("-" * 40)
print(ply2)