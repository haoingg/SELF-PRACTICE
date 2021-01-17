# 이중 리스트
lol = [[1,2,3], [4, 5], [6, 7, 8, 9]]
print(lol[0])
print(lol[2][1])

for sub in lol:
    for item in sub:
        print(item, end = ' ')
    print()

score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]

total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subjects = len(student)
    print("총점 %d, 평균 %.2f" % (sum, sum / subjects))
    total += sum
    totalsub += subjects
print("전체평균 %.2f" % (total / totalsub))

#리스트 컴프리헨션
nums = [n * 2 for n in range(1, 11)]
for i in nums:
    print(i, end = ',')