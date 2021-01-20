while True:
    num = int(input("숫자를 입력하시오 : "))
    if num == 0:
        print("종료")
        break
    elif num < -10 or num > 10:
        continue
    elif num > 0:
        sum=1
        print("입력값 : ", num)
        for i in range(1, num+1):
            sum*=i
        print(sum)
    else:
        sum=1
        print("입력값(부호변경) : ", num)
        num= num*-1
        for i in range(1, num+1):
            sum *= i
        print(sum)

