import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, row, col, w, h):
    q = deque([(row, col)])

    dCol = [-1, -1, -1, 0, 0, 1, 1, 1]
    dRow = [-1, 0, 1, -1, 1, -1, 0, 1]
    graph[row][col] = 0
    while q:
        current = q.popleft()

        for i in range(8):
            nRow = current[0] + dRow[i]
            nCol = current[1] + dCol[i]

            if nRow < 0 or nRow >= h or nCol < 0 or nCol >= w:
                continue
            if graph[nRow][nCol] == 0:
                continue

            graph[nRow][nCol] = 0
            q.append((nRow, nCol))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for row in range(h):
        for col in range(w):
            if graph[row][col] == 1:
                bfs(graph, row, col, w, h)
                result += 1
            # print("row : %d, col : %d" % (row, col))
            # for i in graph:
            #     print(i)

    print(result)
