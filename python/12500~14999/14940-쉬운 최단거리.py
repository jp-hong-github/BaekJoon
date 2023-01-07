import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

start_point = None
for row in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    try:
        col = temp.index(2)
        start_point = (row, col)
    except:
        continue

q = deque([])
q.append(start_point)
distance = [[None for _ in range(m)] for _ in range(n)]
distance[start_point[0]][start_point[1]] = 0

direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while q:
    row, col = q.popleft()
    for dRow, dCol in direction:
        nRow = row + dRow
        nCol = col + dCol
        if 0 <= nRow < n and 0 <= nCol < m and graph[nRow][nCol] != 0:
            if distance[nRow][nCol] is None:
                distance[nRow][nCol] = distance[row][col] + 1
                q.append((nRow, nCol))
            elif distance[nRow][nCol] is not None:
                if distance[nRow][nCol] > distance[row][col] + 1:
                    distance[nRow][nCol] = distance[row][col] + 1
                    q.append((nRow, nCol))

for row in range(n):
    for col in range(m):
        if col == m - 1:
            if graph[row][col] == 0:
                print(0)
            elif distance[row][col] is None:
                print(-1)
            else:
                print(distance[row][col])

        else:

            if graph[row][col] == 0:
                print(0, end=" ")
            elif distance[row][col] is None:
                print(-1, end=" ")
            else:
                print(distance[row][col], end=" ")
