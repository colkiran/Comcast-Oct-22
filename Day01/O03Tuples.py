
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = 3,
print(type(t2))

print("-" * 40)
t3 = (1, 2, 3)
print(t3[1])
# t3[1] = 100

print("-" * 40)
# immutable dictionary

from collections import namedtuple

nmdTpl = namedtuple("Products", "prodid prodname cat prc")
prod = nmdTpl(prodid=101, prodname="KitKat", cat="Choclate", prc=35)

print(prod)
print(f"Prod Id   :{prod.prodid}")
print(f"Prod Name :{prod.prodname}")
print(f"Category  :{prod.cat}")
print(f"Price     :{prod.prc}")

# prod.prc  = 45

