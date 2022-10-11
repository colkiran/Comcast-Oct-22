
def add(x, y):
    return x + y

a = add
print(type(a))
res = a(200, 300)
print(res)

print("-" * 40)
y = lambda a, b: a + b
print(type(y))
res = y(35, 85)
print(res)

# lambda's  are best used with the following functions
# a. map
# b. filter
# c. reduce

# map + lambda => expression of lambda will be implemented on every element of the list given by map

l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

months = ['dec', 'aug', 'nov', 'jan', 'sep', 'apr', 'oct', 'feb', 'may', 'jun', 'mar','jul']
from calendar import month_name

print(f"months    :{months}")
asc_res = sorted(months, key=list(map(lambda mth: mth[0:3].lower(), list(month_name))).index)
print(f"ascending :{asc_res}")

print("-" * 40)
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
from functools import reduce
l = [9, 4, 1, 8, 5, 3, 7, 2, 6, 10]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res1 = reduce(lambda x, y: x + y, l)
print(f"res1 :{res1}")
