"""
self - variable that will hold the name of the object that made a call      to the function

ply1.get_details => ply1 will be stored in self of get_details


"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 30)
ply2.get_details()

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")

ply2.runs = 135
print(f"ply2 :{ply2.__dict__}")
print(f"ply1 :{ply1.__dict__}")

