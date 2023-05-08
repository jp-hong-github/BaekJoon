import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 첫 번째 원소는 벽을 부수지 않았을 때의 이동 거리
# 두 번째 원소는 벽을 부수었을 때의 이동 거리
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

q = deque([(0, 0, 0)])
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

result = -1
while q:
    cRow, cCol, wall_break = q.popleft()

    if cRow == n - 1 and cCol == m - 1:
        result = visited[cRow][cCol][wall_break]
        break

    for dRow, dCol in direction:
        nRow = cRow + dRow
        nCol = cCol + dCol

        if not (0 <= nRow < n and 0 <= nCol < m):
            continue

        if graph[nRow][nCol] == 1 and wall_break == 0:
            q.append((nRow, nCol, 1))
            visited[nRow][nCol][1] = visited[cRow][cCol][0] + 1
        elif graph[nRow][nCol] == 0 and visited[nRow][nCol][wall_break] == 0:
            q.append((nRow, nCol, wall_break))
            visited[nRow][nCol][wall_break] = visited[cRow][cCol][wall_break] + 1

print(result)
