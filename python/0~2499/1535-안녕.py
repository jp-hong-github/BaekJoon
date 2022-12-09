import sys
import heapq

input = sys.stdin.readline

n = int(input())
life_list = [0] + list(map(int, input().split()))
pleasure_list = [0] + list(map(int, input().split()))

# 0-1 배낭문제는 그리디 불가

# cost_effectiveness= [(-(pleasure_list[idx] / life_list[idx]), idx) for idx in range(n)]
# heapq.heapify(cost_effectiveness)
# life = 100
# pleasure = 0
# while cost_effectiveness:
#     value, idx = heapq.heappop(cost_effectiveness)
#     if life_list[idx] < life:
#         pleasure += pleasure_list[idx]
#         life -= life_list[idx]

# print(pleasure)

dp = [[0 for _ in range(100 + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, 100):
        if life_list[i] <= k:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - life_list[i]] + pleasure_list[i])
        else:
            dp[i][k] = dp[i - 1][k]

print(dp[n][99])
