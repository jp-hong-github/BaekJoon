import sys

input = sys.stdin.readline

v, e = list(map(int, input().split()))

graph = [[float("inf") for _ in range(v + 1)] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, v + 1):
    for row in range(1, v + 1):
        for col in range(1, v + 1):
            graph[row][col] = min(graph[row][col], graph[row][k] + graph[k][col])

result = float("inf")

# graph[i][i]의 값이 float('inf')가 아니면 사이클이 존재하였음을 의미
for i in range(1, v + 1):
    result = min(result, graph[i][i])


if result == float("inf"):
    print(-1)
else:
    print(result)
