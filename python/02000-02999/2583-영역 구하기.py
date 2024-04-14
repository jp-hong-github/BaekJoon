import sys
from collections import deque


input = sys.stdin.readline

row, col, k = map(int, input().split())

graph = [[0 for _ in range(col)] for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    area = 1
    while q:
        r, c = q.popleft()

        for dRow, dCol in direction:
            nr = r + dRow
            nc = c + dCol

            if not (0 <= nr < row and 0 <= nc < col):
                continue

            if visited[nr][nc]:
                continue

            if graph[nr][nc] == 1:
                continue

            area += 1
            visited[nr][nc] = True
            q.append((nr, nc))

    return area


result = []
for r in range(row):
    for c in range(col):
        if graph[r][c] != 1 and visited[r][c] != True:
            result.append(bfs(r, c))


print(len(result))
print(*sorted(result))
