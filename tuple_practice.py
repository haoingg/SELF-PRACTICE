import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %분입니다" % (result[0], result[1]))

#convertlist
score = [88, 95, 70, 100, 99]
tu = tuple(score)
#tu[0] = 100
print(tu)
li = list(tu)
li[0] = 100
print(li)