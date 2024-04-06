import sys

input = sys.stdin.readline


def check(n, data):
    temp = [[0 for _ in range(n)] for __ in range(2)]
    temp[0][0] = data[0][0]
    temp[1][0] = data[1][0]
    if n >= 2:
        temp[0][1] = data[1][0] + data[0][1]
        temp[1][1] = data[1][1] + data[0][0]
        if n >= 3:
            for u in range(2, n):
                temp[0][u] = max(temp[1][u - 2], temp[1][u - 1]) + data[0][u]
                temp[1][u] = max(temp[0][u - 2], temp[0][u - 1]) + data[1][u]
            # for q in temp:
            #     print(q)
            return max(temp[0][n - 1], temp[1][n - 1], temp[0][n - 2], temp[1][n - 2])
        else:
            return max(temp[0][1], temp[1][1])
    else:
        return max(temp[0][0], temp[1][0])


t = int(input())
for i in range(t):
    data = []
    n = int(input())
    data.append(list(map(int, input().split())))
    data.append(list(map(int, input().split())))
    print(check(n, data))
