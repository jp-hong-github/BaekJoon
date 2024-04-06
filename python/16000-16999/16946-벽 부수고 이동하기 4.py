import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append([int(i) for i in input().rstrip()])


# 벽이 없는 곳에서의 영역의 칸의 개수 세기(검색해보니 플러드 필 알고리즘이라고 한다.)
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for row in range(n):
    for col in range(m):
        if graph[row][col] == 0:
            q = deque([(row, col)])
            graph[row][col] = -1
            area_count = 1  # 해당 영역의 벽이 아닌 칸의 개수
            wall_set = set()  # 해당 영역 주변에 있는 벽

            # bfs
            while q:
                cRow, cCol = q.popleft()

                for dRow, dCol in direction:
                    nRow = cRow + dRow
                    nCol = cCol + dCol

                    if not (0 <= nRow < n and 0 <= nCol < m):
                        continue

                    if graph[nRow][nCol] == 0:
                        graph[nRow][nCol] = -1
                        area_count += 1
                        q.append((nRow, nCol))

                    elif graph[nRow][nCol] >= 1:
                        wall_set.add((nRow, nCol))

            # 벽에 대해 바로 계산
            while wall_set:
                wall_row, wall_col = wall_set.pop()
                graph[wall_row][wall_col] += area_count % 10


for r in range(n):
    for c in range(m):
        if graph[r][c] == -1:
            print(0, end="")
        else:
            print(graph[r][c] % 10, end="")
    print()
