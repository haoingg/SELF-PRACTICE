import random
a = 0

while True:
    b = random.randint(0, 30)
    if (27 <= b <= 30) or 0:
        break
    else:
        a += 1
        print(chr(b+64),"(",b,")")

print("수행횟수는", a, "번입니다")