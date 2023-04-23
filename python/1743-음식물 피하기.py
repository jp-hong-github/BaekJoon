import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())

# 1 이면 쓰레기, 0이면 아무것도 없음
graph = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

# 그래프 채우기
for i in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

# bfs
def bfs(graph, row, col):
    q = deque([(row, col)])
    size = 0

    dRow = [-1, 1, 0, 0]
    dCol = [0, 0, -1, 1]

    graph[row][col] = 0
    size += 1
    while q:
        cRow, cCol = q.popleft()

        for i in range(4):
            nRow = cRow + dRow[i]
            nCol = cCol + dCol[i]
            if nRow < 0 or nRow > n or nCol < 0 or nCol > m:
                continue
            if graph[nRow][nCol] == 1:
                graph[nRow][nCol] = 0
                size += 1
                # print("nRow,nCol : ", nRow, nCol)
                q.append((nRow, nCol))
    return size


# for i in graph:
#     print(i)
# 계산
result = 0
for row in range(1, n + 1):
    for col in range(1, m + 1):
        if graph[row][col] == 1:
            temp = bfs(graph, row, col)
            if result < temp:
                result = temp

# 결과 출력
print(result)
# print(graph)
