import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# BFS 알고리즘
def bfs_no_color_blind(graph, n, visited, row, col):
    if visited[row][col]:
        return 0

    q = deque()
    q.append((row, col))
    visited[row][col] = True
    color = graph[row][col]

    while q:
        cRow, cCol = q.popleft()

        for dRow, dCol in direction:
            nRow = cRow + dRow
            nCol = cCol + dCol
            if not (0 <= nRow < n and 0 <= nCol < n):
                continue

            if visited[nRow][nCol]:
                continue

            if not (color == graph[nRow][nCol]):
                continue

            visited[nRow][nCol] = True
            q.append((nRow, nCol))

    return 1


# BFS 알고리즘
def bfs_color_blind(graph, n, visited, row, col):
    if visited[row][col]:
        return 0

    q = deque()
    q.append((row, col))
    visited[row][col] = True
    color = graph[row][col]

    while q:
        cRow, cCol = q.popleft()

        for dRow, dCol in direction:
            nRow = cRow + dRow
            nCol = cCol + dCol
            if not (0 <= nRow < n and 0 <= nCol < n):
                continue

            if visited[nRow][nCol]:
                continue

            if ((color == "R" or color == "G") and graph[nRow][nCol] == "B") or (
                color == "B" and (graph[nRow][nCol] == "R" or graph[nRow][nCol] == "G")
            ):
                continue

            visited[nRow][nCol] = True
            q.append((nRow, nCol))

    return 1


result = {"color blindness": 0, "no color blindness": 0}
visited_color_blind = [[False for _ in range(n)] for _ in range(n)]
visited_no_color_blind = [[False for _ in range(n)] for _ in range(n)]
for r in range(n):
    for c in range(n):
        result["color blindness"] += bfs_color_blind(
            graph, n, visited_color_blind, r, c
        )
        result["no color blindness"] += bfs_no_color_blind(
            graph, n, visited_no_color_blind, r, c
        )

print(result["no color blindness"], result["color blindness"])
