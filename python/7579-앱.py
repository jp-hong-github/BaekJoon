import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
apps = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
costs_sum = sum(costs)

dp = [[0 for _ in range(costs_sum + 1)] for _ in range(n + 1)]

result = float("inf")
for app in range(1, n + 1):
    for cost in range(1, costs_sum + 1):
        if costs[app] > cost:
            dp[app][cost] = dp[app - 1][cost]
        else:
            dp[app][cost] = max(dp[app - 1][cost], apps[app] + dp[app - 1][cost - costs[app]])
            if dp[app][cost] >= m:
                result = min(result, cost)


print(result)
