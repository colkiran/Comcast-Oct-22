
fruits = [
    ('apple', 280),
    ('orange', 180),
    ('grapes', 140),
    ('pineapple', 80),
    ('gauva', 90),
    ('banana', 55),
    ('strawberry', 350),
    ('watermelon', 70)
]

print(f"fruits :{fruits}")

print("-" * 40)
prices = ["fruit" for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[0] for fruit in fruits]
print(prices)

print("-" * 40)
prices= [fruit[1] for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] * 0.9 for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] * 0.75 for fruit in fruits]
print(prices)

print("-" * 40)
prices = [(fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits ]
print(prices)

print("-" * 40)
expPrdt = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] >= 100]
print(expPrdt )