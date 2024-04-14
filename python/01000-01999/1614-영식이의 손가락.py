injured_finger = int(input())
limit = int(input())

if injured_finger == 2 or injured_finger == 3 or injured_finger == 4:
    if limit % 2 == 0:  # 짝수인 경우
        print(4 * limit + injured_finger - 1, end="")
    else:  # 홀수인 경우
        print(4 * limit + 5 - injured_finger)
elif injured_finger == 1:  # 엄지를 다쳤을 경우
    print(8 * limit, end="")
elif injured_finger == 5:  # 새끼를 다쳤을 경우
    print(4 + 8 * (limit), end="")
