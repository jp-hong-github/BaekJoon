import sys
import math
from collections import deque

input = sys.stdin.readline

m, n = list(map(int, input().split()))

tomato_already = []  # 이미 익은 토마토
graph = []
visited = [[-1 for _ in range(m)] for _ in range(n)]

for row in range(n):
    temp = list(map(int, input().split()))
    for col, tomato in enumerate(temp):
        if tomato == 1:
            visited[row][col] = 0
            tomato_already.append((row, col))

    graph.append(temp)


q = deque(tomato_already)

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while q:
    cRow, cCol = q.popleft()

    for dRow, dCol in direction:
        nRow = cRow + dRow
        nCol = cCol + dCol

        if 0 <= nRow < n and 0 <= nCol < m:
            if graph[nRow][nCol] != -1 and (
                visited[nRow][nCol] > visited[cRow][cCol] + 1
                or visited[nRow][nCol] == -1
            ):
                visited[nRow][nCol] = visited[cRow][cCol] + 1
                q.append((nRow, nCol))

no_good_tomato = False  # 안 익은 토마토 확인
result = 0
for row in range(n):
    for col in range(m):
        result = max(result, visited[row][col])
        if visited[row][col] == -1 and graph[row][col] == 0:
            no_good_tomato = True
            break

    if no_good_tomato:
        break

# 안 익은 토마토가 존재
if no_good_tomato:
    print(-1)
else:
    print(result)
