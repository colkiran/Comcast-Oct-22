
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Australia', 'venue': 'Perth'}
print(f"player :{player}")

print(f"Name     :{player['name']}")
print(f"Opponent :{player['oppn']}")

print("-" * 40)
for i in player:
    print(i, "=>", player[i])

print("-" * 40)
# print(dir(player))
k = player.keys()
print(k)
v = player.values()
print(v)
print("-" * 40)

for k, v in player.items():
    print(k + "=>" + str(v))

print("-" * 40)
# list into a dictionary
cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")

res = dict.fromkeys(cities)
print(f'res :{res}')

res1 = dict.fromkeys(cities, 21)
print(f"res1 :{res1}")
