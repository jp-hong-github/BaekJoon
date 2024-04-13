import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().strip()) for _ in range(R)]
result = 0


def bfs(graph, start_vertex):
    queue = deque([start_vertex])

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue

            if graph[nr][nc] == ".":
                continue

            if graph[nr][nc] == "#":
                graph[nr][nc] = "."
                queue.append((nr, nc))


for r in range(R):
    for c in range(C):
        if graph[r][c] == "#":
            bfs(graph, (r, c))
            result += 1


print(result)
