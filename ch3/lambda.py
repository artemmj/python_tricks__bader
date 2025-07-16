add = lambda x, y: x + y
print(add(5, 10))
print((lambda x, y: x + y)(5, 9))

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[0]))

print(sorted(range(-5, 6), key=lambda x: x * x))
