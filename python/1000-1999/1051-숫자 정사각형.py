import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
result = 0

# 브루트포스 알고리즘
for length in range(0, min(N, M)):
    for row in range(0, N - length):
        for col in range(0, M - length):
            value = graph[row][col]
            if value != graph[row + length][col] or value != graph[row][col + length] or value != graph[row + length][col + length]:
                continue
            else:
                result = max(result, (length + 1) ** 2)


print(result)
