class Player:                   # pascal casing

    def __init__(self):         # constructor __init__ double
        print("player initialized....")
                                # underscore init - dunder-init


    def get_runs(self):
        print("runs scored.....")

sachin = Player()           # implicitly call the constructor
sachin.get_runs()

print("-" * 40)
rahul = Player()
rahul.get_runs()

print("-" * 40)
sachin.__init__()

print("-" * 40)
print(f"isinstance(sachin, Player) : {isinstance(sachin, Player)}")
print(f"isinstance(sachin, object) : {isinstance(sachin, object)}")
print(f"isinstance(sachin, str) : {isinstance(sachin, str)}")

