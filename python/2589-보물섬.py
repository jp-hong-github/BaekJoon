import sys
from collections import deque

input = sys.stdin.readline

ROW, COL = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(ROW)]

result = -1


def bfs(row, col):
    global result
    visited = [[False for _ in range(COL)] for _ in range(ROW)]

    q = deque([(row, col, 0)])  # 세 번째 값은 시간
    visited[row][col] = True
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while q:
        cr, cc, ct = q.popleft()
        for dRow, dCol in direction:
            nr = cr + dRow
            nc = cc + dCol
            if not (0 <= nr < ROW and 0 <= nc < COL):
                continue

            if graph[nr][nc] == "W":
                continue

            if visited[nr][nc] == True:
                continue

            q.append((nr, nc, ct + 1))
            visited[nr][nc] = True
            result = max(result, ct + 1)


for r in range(ROW):
    for c in range(COL):
        if graph[r][c] != "W":
            bfs(r, c)

print(result)
