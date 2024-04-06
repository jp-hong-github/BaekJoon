import sys
from collections import deque

input = sys.stdin.readline

ROW, COL = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(ROW)]

visited = [[False for _ in range(COL)] for _ in range(ROW)]

result = 0

# 8 방향
direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


# BFS 사용
def bfs(r, c):
    is_mountaintop = True

    global result

    q = deque([(r, c)])
    current_height = graph[r][c]
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()
        for dr, dc in direction:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr < ROW and 0 <= nc < COL):
                continue

            # 현재 산의 높이보다 작은 경우 통과
            if graph[nr][nc] < current_height:
                continue

            # 주변에 현재 산의 위치보다 높은 경우 산봉우리가 아님
            # 중단해도 상관없으나 visited를 채우기 위해 로직은 계속 수행
            if graph[nr][nc] > current_height:
                is_mountaintop = False
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            q.append((nr, nc))

    if is_mountaintop:
        result += 1


for r in range(ROW):
    for c in range(COL):
        if graph[r][c] == 0:
            visited[r][c] = True
        elif not visited[r][c]:
            bfs(r, c)

print(result)
