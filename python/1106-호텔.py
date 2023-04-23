import sys
import heapq

input = sys.stdin.readline
c, n = map(int, input().split())

city = []
for _ in range(n):
    money, customers = map(int, input().split())
    efficiency = customers / money
    city.append([efficiency, customers, money])

city.sort(key=lambda x: [-int(x[0]), int(x[1])])
dp = [int(10e9) for _ in range(1000 + 1)]
dp[0] = 0

for i in range(1, 1000 + 1):
    for k in range(i):
        for case in city:
            if case[1] >= i - k: # ! 최소라는 것이 중요
                dp[i] = min(dp[i], dp[k] + case[2])


print(min(dp[c:]))
# print(dp[c : c + 10])
