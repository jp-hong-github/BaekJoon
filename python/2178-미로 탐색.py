import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

INF = int(10e9)
move_count = [[INF for _ in range(M)] for __ in range(N)]

q = deque([(0, 0)])
move_count[0][0] = 1

dRow = [0, 0, -1, 1]
dCol = [-1, 1, 0, 0]
while q:
    row, col = deque.popleft(q)
    current_move_count = move_count[row][col]
    for i in range(4):
        nRow, nCol = (row + dRow[i], col + dCol[i])
        if (0 <= nRow and nRow <= N - 1) and (0 <= nCol and nCol <= M - 1):
            if graph[nRow][nCol] == 1:
                if move_count[nRow][nCol] > current_move_count + 1:
                    q.append((nRow, nCol))
                    move_count[nRow][nCol] = current_move_count + 1

print(move_count[N - 1][M - 1])
