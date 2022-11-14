import sys

input = sys.stdin.readline

N = int(input())

numList = [0 for _ in range(10000001)]
len_numList = 1


def cal(digit, num, arr):
    global len_numList
    # print(digit, num, arr, len_numList)
    if len(arr) == digit:
        numList[len_numList] = arr.copy()
        len_numList += 1

    else:
        for i in range(0, num, 1):
            arr.append(i)
            cal(digit, i, arr)
            arr.pop()


digit = 1
for digit in range(1, 11):
    for i in range(1, 10):
        arr = [i]
        cal(digit, i, arr)

if numList[N] == 0 and N != 0:
    print(-1)
elif N == 0:
    print(0)
else:
    result = 0
    for num in numList[N]:
        result *= 10
        result += num
    print(result)
