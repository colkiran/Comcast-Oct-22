
# inheritance
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor.....")


    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly.......")


class Fish(Animal):

    def swim(self):
        print("Fishes swim.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 40)

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 40)
print(f"isinstance(cuckoo, Bird)    :{isinstance(cuckoo, Bird)}")
print(f"isinstance(cuckoo, Animal)  :{isinstance(cuckoo, Animal)}")
print(f"isinstance(dolphin, Fish)   :{isinstance(dolphin, Fish)}")
print(f"isinstance(dolphin, Animal) :{isinstance(dolphin, Animal)}")

print("-" * 40)
print(f"isinstance(dolphin, Bird)  :{isinstance(dolphin, Bird)}")
print(f"isinstance(cuckoo, Animal) :{isinstance(cuckoo, Fish)}")
