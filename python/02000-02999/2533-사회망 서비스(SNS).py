import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# [해당 노드가 얼리어답터인 경우, 해당 노드가 얼리어답터가 아닌 경우]
dp = [[1, 0] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]


def dfs(current):
    visited[current] = True
    for child in tree[current]:
        # dfs(child)
        if not visited[child]:
            dfs(child)
            dp[current][0] += min(dp[child][0], dp[child][1])
            dp[current][1] += dp[child][0]


dfs(1)
print(min(dp[1]))
