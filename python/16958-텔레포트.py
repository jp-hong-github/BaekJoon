import sys
from itertools import combinations

input = sys.stdin.readline

n, t = map(int, input().split())
cities: list = []
for i in range(n):
    s, x, y = map(int, input().split())
    cities.append((s, x, y))

# 그래프 초기화
INF = 10000
graph = [[INF for _ in range(n)] for _ in range(n)]
comb = combinations(range(n), 2)
for x, y in comb:
    dist = abs(cities[x][1] - cities[y][1]) + abs(cities[x][2] - cities[y][2])

    if cities[x][0] == 1 and cities[y][0] == 1 and t < dist:
        graph[x][y] = t
        graph[y][x] = t
    else:
        graph[x][y] = dist
        graph[y][x] = dist


# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if k == j or j == i or i == k:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(graph[a - 1][b - 1])
