
class Player():

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Virat", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rohit", 33)
ply2.get_details()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
ply1.team = "RCB"
print(f"ply1 :{ply1.team}")
print(f"Player :{Player.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
print(ply1.__dict__)        # cannot change the data in class
                            # attribute using objects

print("-" * 40)
print(Player.__dict__)
