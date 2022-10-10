

l1 = list()
print(f"l1 :{l1}")
print(type(l1))                 # RTTI - Runtime Type Identification
print('-' * 40)

l2 = [1, 2, 3, 4.5, 5.6, 6.3, 'seven', 'eight', 'nine', 10+0j, 11-2j, True, False ]
print(f"l2 :{l2}")          # formatting - interpolation -
print('-' * 40)

print("1 :", id(l2[0]))
print("2 :", id(l2[1]))
print("3   :", id(l2[2]))
print("4.5 :", id(l2[3]))

print('-' * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(len(l3))

# indexed and reverse indexed

# indexed - 0, 1, 2, 3.....
# reverse index - -1, -2, -3....

print(f"l3[0] :{l3[0]}")
print(f"l3[5] :{l3[5]}")
print(f"l3[9] :{l3[9]}")
# print(f"l3[9] :{l3[10]}")

print(f"l3[-1] :{l3[-1]}")
print(f"l3[-6] :{l3[-6]}")
print(f"l3[-10] :{l3[-10]}")

print(l3[0:5])
print(l3[5:10])

print(l3[-1:-7:-1])
print(l3[-5:-11:-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1 * 2)
l3 = [l1, l2]
print(f"l3 :{l3}")
print(len(l3))

l4 = [*l1, *l2]
print(len(l4))
print(l4)

print('-' * 40)
l1 = [1, 2, 3, 4, 5]
l1[2] = 2.5
print(l1)

l1 = [1, 2, 3, 4, 5]
res = l1.insert(2, 33)
print(f"l1 :{l1}")

l1.insert(50, 10)
print(F"l1 :{l1}")

print('-' * 40)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l2 = l1                     # shallow copy - copying the address with the data
print(f"l2 :{l2}")
l1.extend([6, 7, 8])
print(f"l1 :{l1}")
print(f"l2 :{l2}")

print('-' * 40)
l3 = [1, 2, 3, 4, 5]
print(f"l3 :{l3}")
l4 = l3.copy()              # deep copy - only shared
print(f"l4 :{l4}")
l4.extend([66, 77, 88])
print(f"l4 :{l4}")
print(f"l3 :{l3}")

print('-' * 40)
l1 = [1, 2, 3, 4, [10, 20, 30, 40, 50] ,5]
print(f"l1 :{l1}")

l2 = l1.copy()              # deep copy
print(f"l2 :{l2}")

l1[4].extend([60, 70, 80])
print(f"l1[4] :{l1[4]}")
print(f"l2[4] :{l2[4]}")

print('-' * 40)
from copy import deepcopy
l1 = [1, 2, 3, [5, 10, 15, 20], 4]
print(F"l1 :{l1}")
l2 = deepcopy(l1)
print(f"l2 :{l2}")

l2[3].extend([5, 6, 7, 8])
print(f"l1 :{l1}")
print(f"l2 :{l2}")

print('-' * 40)
l1 = [10, 6, 9, 5, 8, 4, 2, 7, 1, 3]
print(f"l1 :{l1}")

# sort      - will sort the original list
# sorted    - will take a copy of the list and sorts it

asc_res  = sorted(l1)
print(f"Ascending  :{asc_res}")
desc_res  = sorted(l1, reverse=True)
print(f"Descending :{desc_res}")

print('-' * 40)
l1 = [10, 'zebra', 6, 'apple', 9, 'yellow', 5, 'blue', 8, 'white', 4, 'green', 2, 'violet', 7, 'maroon', 1, 'pink', 3, 'dog', 'cat']
print(f"l1 :{l1}")

print('-' * 40)
asc_res = sorted(l1, key=ascii)
print(f"Ascending :{asc_res}")

print('-' * 40)

cities = ['thiruvananthapuram', 'chennai', 'bangalore', 'delhi', 'ooty', 'hyderabad']
print(f"cities :{cities}")

print('-' * 40)
asc_res = sorted(cities, key=len)
print(f"Ascending :{asc_res}")

print('-' * 40)
months = ['dec', 'aug', 'nov', 'jan', 'sep', 'apr', 'oct', 'feb', 'may', 'jun', 'mar','jul']

# sort these months

from calendar import month_name

print(list(month_name))

l = []
for mon in list(month_name):
    l.append(mon[0:3].lower())

print(f"l :{l}")

def sort_month(mon):
    if mon in l:
        return l.index(mon)

print('-' * 40)
print(f"months :{months}")

print('-' * 40)
asc_res = sorted(months, key=sort_month)
print(f"Ascending :{asc_res}")
