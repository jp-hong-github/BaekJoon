import sys

input = sys.stdin.readline

n = int(input())
# graph = [[INF for _ in range(n)] for __ in range(n)]
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] != 0 and graph[k][b] != 0:
                graph[a][b] = max(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if graph[a][b] > 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
