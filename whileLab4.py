while True:
    month = int(input("월을 입력하세요 :"))

    if 3 <= month <= 5:
        print(month, "월은 봄")
    elif 6 <= month <= 8:
        print(month, "월은 여름")
    elif 9 <= month <= 11:
        print(month, "월은 가을")
    elif month == 12 or 1 <= month <=2:
        print(month, "월은 겨을")
    else:
        print("1~12 사이의 값을 입력하세요!")
        break
