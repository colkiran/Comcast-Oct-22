
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = val

    def del_price(self):
        self.__price =0

import sys
try:
    p1 = Product(50)
    print(p1)
    p1.set_price(200)
    print(p1.get_price())
    p1.set_price(500)
    print(p1.get_price())
    p1.del_price()
    print(p1.get_price())

except ValueError:
    print('Error Occured.......')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

