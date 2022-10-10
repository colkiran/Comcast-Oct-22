
s1 = {1, 2, 3, 4, 5, True, False, 'seven', 'eight', 'nine', 'ten'}
print(f"s1 :{s1}")

print("-" * 40)
# s2 = {1, 2, 3, [10, 20, 30], 5}
s3 = {1, 2, 3, (10, 20, 30), 5}
# s4 = {1, 2, 3, {'a', 'apple', 'b', 'ball'}, 5}

# print(s2)
print(s3)
# print(s4)

s1 = {1, 2, 3, 4, 5, 6}
s1.add(7)
s1.add(2)

s1.update([8, 9, 10])
print(f"s1 :{s1}")
print("-" * 40)

# s1.pop()
# s1.remove()
# s1.discard()

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A Symmetric_difference B :", A ^ B)
print("B Symmetric_difference A :", B.symmetric_difference(A))

print("-" * 40)
c = frozenset([1, 2, 3, 4, 5])
print(f"c :{c}")
print(type(c))
