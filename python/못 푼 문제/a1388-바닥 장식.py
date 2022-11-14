from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))

dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]


def bfs(row, col):
    q = deque()
    q.append((row, col))

    while q:
        row, col = q.popleft()
        
    for i in range(4):
        nRow = dRow[i] + row
        nCol = dCol[i] + col

        if nRow<0 or nRow>=n or  nCol<0 or nCol>=m:
            continue
        if graph[nRow][nCol] == graph[row][col]:
            