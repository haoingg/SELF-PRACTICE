str = "100점"
try:
    score=int(str)
    print(score)
except:
    print("예외가 발생했습니다")
print("작업 완료")

#무한루프 while일 때
while True:
    str = input("여기에 점수를 입력하세요: ")
    try:
        score = int(str)
        print("점수 :", score)
        break
    except:
        print("예외가 발생했습니다")
print("작업 완료")


#raise
def a(n):
    if (n<0):
        return ValueError
    sum = 0
    for i in range(n+1):
        sum += sum + i
    return sum

try:
    print("~10 =", a(10))
    print("~5 =", a(-5))
except ValueError:
    print("입력 값이 잘못됐습니다")
