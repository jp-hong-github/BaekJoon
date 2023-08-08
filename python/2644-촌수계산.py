import sys

input = sys.stdin.readline

from collections import deque


def bfs(graph, start, end, visited):
    q = deque([(start, 0)])
    visited[start] = 0
    count = 0
    while q:
        v = q.popleft()
        count = v[1] + 1
        for i in graph[v[0]]:
            if visited[i] == -1:
                q.append((i, v[1] + 1))
                visited[i] = v[1] + 1


n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

result = -1
visited = [-1 for _ in range(n + 1)]

bfs(graph, a, b, visited)

if visited[b] == -1:
    print(-1)
else:
    print(abs(visited[a] - visited[b]))
