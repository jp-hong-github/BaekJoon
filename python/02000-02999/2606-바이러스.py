import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

from collections import deque

q = deque([1])
visited = [False for _ in range(n + 1)]
visited[1] = True

while q:
    cur = q.popleft()
    for next in graph[cur]:
        if visited[next] is False:
            visited[next] = True
            q.append(next)

print(visited.count(True) - 1)
