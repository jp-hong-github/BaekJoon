import sys

input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(10)], [1 for _ in range(10)]]

for c in range(2, 1001):
    temp = []
    for i in range(0, 10):
        temp_i = 0
        for k in range(0, i + 1):
            temp_i += dp[c - 1][k]
        temp.append(temp_i)
    dp.append(temp)

result = 0
for val in dp[N]:
    result += val % 10007

print(result % 10007)
