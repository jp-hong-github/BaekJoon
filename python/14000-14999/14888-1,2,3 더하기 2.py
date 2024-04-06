import sys

input = sys.stdin.readline

n, k = map(int, input().split())

result = []


def cal(value, numList, current_sum):
    if current_sum == n:
        result.append(numList.copy())
    elif current_sum > n:
        return
    else:
        for i in range(1, 4):
            numList.append(i)
            cal(i, numList, current_sum + i)
            numList.pop()


numList = []
cal(0, numList, 0)
# print(result)
if len(result) <= k - 1:
    print(-1)
else:
    for num in range(0, len(result[k - 1])):
        if num != len(result[k - 1]) - 1:
            print("%d+" % (result[k - 1][num]), end="")
        else:
            print("%d" % (result[k - 1][num]))
