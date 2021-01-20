import random

a = 1
b = random.randint(5, 10)

while a <= b:
    print(a, "->", a ** 2)
    a += 1