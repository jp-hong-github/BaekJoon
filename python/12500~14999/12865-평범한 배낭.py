import sys

input = sys.stdin.readline

n, k = map(int, input().split())

data = []

for _ in range(n):
    w, v = map(int, input().split())
    data.append([w, v]) # [무게, 가치]

data.sort(key=lambda x: [x[0], -x[1]])

dp = [0] * (k + 1)

result = 0
for i in range(n):
    for weight in range(k, 1, -1):
        if data[i][0] <= weight:
            dp[weight] = max(dp[weight], dp[weight - data[i][0]] + data[i][1])


print(dp[k])
