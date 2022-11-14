import sys

input = sys.stdin.readline

# n이 행, m이 열
n, m = map(int, input().split())

graph = []

doyeon = (-1, -1)  # 도연이의 위치
c = False  # 도연이를 찾았는지 확인하는 변수
for z in range(n):
    temp = list(map(str, input().rstrip()))
    if not c and "I" in temp:
        x = temp.index("I")
        doyeon = (x, z)
        c = True
    graph.append(temp)

visited = [[False for _ in range(m)] for __ in range(n)]

from collections import deque

q = deque([doyeon])

dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]
result = 0
while q:
    col, row = q.popleft()

    for i in range(4):
        nRow = dRow[i] + row
        nCol = dCol[i] + col

        if nRow < 0 or nRow >= n or nCol < 0 or nCol >= m or graph[nRow][nCol] == "X":
            continue
        if visited[nRow][nCol] == True:
            continue

        visited[nRow][nCol] = True
        q.append((nCol, nRow))

        if graph[nRow][nCol] == "P":
            result += 1

# for i in visited   :
#     print(i)
if result == 0:
    print("TT")
else:
    print(result)
