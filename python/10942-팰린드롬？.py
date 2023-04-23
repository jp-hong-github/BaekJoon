import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

dp = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = True

for i in range(2, n):
    for j in range(n - i):
        if numbers[j] == numbers[j + i] and dp[j + 1][j + i - 1] is True:
            dp[j][i + j] = True

for _ in range(m):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    if dp[start][end] is True:
        print(1)
    elif dp[start][end] is False:
        print(0)


# for i in dp:
#     print(i)
