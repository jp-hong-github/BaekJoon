from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
pair = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(pair):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n + 1)]


def bfs(start):
    q = deque([start])
    result = 0
    while q:
        current = q.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                result += 1
                q.append(next)
    return result


print(bfs(1) - 1)
# print(graph)
# print(visited)
