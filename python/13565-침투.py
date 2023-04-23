import sys

input = sys.stdin.readline

ROW, COL = map(int, input().split())
graph = []
for _ in range(ROW):
    graph.append(list(map(int, input().rstrip())))


dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]

# bfs

from collections import deque


def bfs(row, col):
    q = deque([(row, col)])
    while q:
        cRow, cCol = q.popleft()
        for i in range(4):
            nRow = cRow + dRow[i]
            nCol = cCol + dCol[i]
            if nRow < 0 or nCol < 0 or nRow >= ROW or nCol >= COL:
                continue
            # 벽인 경우 무시
            if graph[nRow][nCol] == 1:
                continue
            if graph[nRow][nCol] == 0:
                graph[nRow][nCol] = 2
                q.append((nRow, nCol))


for i in range(COL):
    bfs(0, i)


flag = 0
for k in range(COL):
    if graph[ROW - 1][k] == 2:
        flag = 1
        break

if flag == 0:
    print("NO")
else:
    print("YES")

# for q in graph:
#     print(q)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# dfs로 풀면 메모리 초과됨
# 질문 검색 살펴보니 파이썬 dfs로는 못 푸는 것 같음

# sys.setrecursionlimit(10 ** 9)

# # dfs
# def dfs(row, col):
#     if row < 0 or col < 0 or row >= ROW or col >= COL:  # 그래프 바깥을 벗어나는 경우
#         return
#     if graph[row][col] != 0:  # 벽이거나 지난 자리일 경우
#         return
#     if graph[row][col] == 0:
#         graph[row][col] = 2  # 지나간 자리를 2로 한다
#         dfs(row - 1, col)
#         dfs(row, col - 1)
#         dfs(row + 1, col)
#         dfs(row, col + 1)
#         return
#     return


# for i in range(COL):
#     dfs(0, i)

# final_result = 0
# for k in range(COL):
#     if graph[ROW - 1][k] == 2:
#         final_result = 1
#         break

# if final_result == 0:
#     print("NO")
# else:
#     print("YES")

