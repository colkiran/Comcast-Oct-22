
class Player():

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    # @classmethod
    # def ChangeTeam(cls, tm):
    #     cls.team = tm

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("factory...")
        return cls(f"{fname} {lname}", age)


ply1 = Player.CreatePlayer("Sunil", "Gavaskar", 67)
ply1.get_details()

print("-" * 40)






"""
print("-" * 40)
Player.ChangeTeam("KKR")

print(Player.team)
"""