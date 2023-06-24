import sys

input = sys.stdin.readline

row, col = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(row)]

dp = [[0 for _ in range(col)] for _ in range(row)]


for r in range(row):
    for c in range(col):
        if r == 0:
            # 맨 왼쪽 위
            if c == 0:
                dp[r][c] = graph[r][c]
            # 맨 위쪽 줄
            else:
                dp[r][c] = dp[r][c - 1] + graph[r][c]
        # 맨 왼쪽 줄
        elif c == 0:
            dp[r][c] = dp[r - 1][c] + graph[r][c]
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]) + graph[r][c]

print(dp[row - 1][col - 1])
