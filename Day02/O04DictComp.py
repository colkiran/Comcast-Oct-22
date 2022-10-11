
d1 = [x ** 2 for x in range(1, 11)]
print(f"d1 :{d1}")

players = {
    'sachin': [290, 350, 460, 401, 380],
    'rahul': [230, 410, 185, 275, 370],
    'sehwag': [380, 430, 485, 390, 350],
    'sourav': [140, 190, 385, 430, 320],
    'yuvraj': [160, 230, 380, 130, 184]
}


print(f"players :{players}")

print("-" * 40)
print(f"sachin :{players['sachin']}")

print("-" * 40)
print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)
scores = {k :sum(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
scores = {k: (lambda scores: sum(scores) / len(scores))(v)
          for k, v in players.items()}
print(f"scores :{scores}")

players = {
    'sachin': [290, 350, 460, 401, 380],
    'rahul': [230, 410, 185, 275, 370],
    'sehwag': [380, 430, 485, 390, 350],
    'sourav': [140, 190, 385, 430, 320],
    'yuvraj': [160, 230, 380, 130, 184]
}

print("-" * 40)
scores = [score for score in players]
print(scores)

print("-" * 40)
scores = [score for score in players.values()]
print(scores)

print("-" * 40)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(scores)

print("-" * 40)
scores = {name : [scr for scr in score if scr >= 200]
          for name, score in players.items()}
print(f"scores  :{scores}")
