

class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called....")
        return self.__price

    @price.setter
    def price(self, val):
        print("setter called....")
        self.__price = val

    @price.deleter
    def price(self):
        print("deleter called.....")
        self.__price = 0


pepsi = Product(25)
print(pepsi.price)

print("-" * 40)
pepsi.price = 50
print(pepsi.price)

print("-" * 40)
del pepsi.price
print(pepsi.price)

print("-" * 40)
pepsi.price = 65
print(pepsi.price)