import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [0]
visited = [False for _ in range(n + 1)]

for i in range(n):
    graph.append([])

for _ in range(m):
    start, destination = map(int, input().split())
    graph[start].append(destination)


def bfs(graph, start):
    q = deque([start])

    while q:
        current = q.popleft()

        for next in graph[current]:
            if next != x and (
                visited[next] == False or visited[next] > visited[current] + 1
            ):
                visited[next] = visited[current] + 1
                q.append(next)


bfs(graph, x)
result = 0
for i in range(n + 1):
    if visited[i] == k:
        print(i)
        result = 1

if result == 0:
    print(-1)

