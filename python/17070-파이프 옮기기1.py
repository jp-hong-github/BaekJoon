# cSpell:disable
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

# ! bfs로 풀 경우 시간 초과(질문 검색에서도 dp로 풀 것을 권장)
######################################################################
# bfs
# q = deque([(0, 1, "GARO")])

# garoNextMove = [(0, 1, "GARO"), (1, 1, "DAEGAK")]
# seroNextMove = [(1, 0, "SERO"), (1, 1, "DAEGAK")]
# daegakNextMove = [(1, 0, "SERO"), (0, 1, "GARO"), (1, 1, "DAEGAK")]

# if graph[N - 1][N - 1] == 1:
#     print(0)
# else:

#     result = 0
#     while q:
#         row, col, shape = q.popleft()
#         # print(row, col, shape)
#         if row == N - 1 and col == N - 1 and graph[N - 1][N - 1] != 1:
#             result += 1
#             continue
#         nextMove = []
#         if shape == "GARO":
#             nextMove = garoNextMove
#         elif shape == "SERO":
#             nextMove = seroNextMove
#         else:
#             nextMove = daegakNextMove
#         for dRow, dCol, nextShape in nextMove:
#             nRow = row + dRow
#             nCol = col + dCol
#             if nRow < 0 or nCol < 0 or nRow >= N or nCol >= N:
#                 continue
#             if graph[nRow][nCol] == 1:
#                 continue
#             if nextShape == "DAEGAK":
#                 if (graph[nRow - 1][nCol] == 1) or (graph[nRow][nCol - 1] == 1):
#                     continue
#             q.append((nRow, nCol, nextShape))

#     print(result)
######################################################################

dp = [[[0, 0, 0] for _ in range(N)] for __ in range(N)]  # 가로,세로,대각선
dp[0][1][0] = 1
for i in range(2, N):
    if graph[0][i] == 0:
        dp[0][i][0] = dp[0][i - 1][0]
for row in range(1, N):
    for col in range(2, N):
        if graph[row][col] == 0:
            dp[row][col][0] = dp[row][col - 1][0] + dp[row][col - 1][2]  # 가로로 가기
            dp[row][col][1] = dp[row - 1][col][1] + dp[row - 1][col][2]  # 세로로 가기
            if graph[row - 1][col] == 0 and graph[row][col - 1] == 0:
                dp[row][col][2] = (
                    dp[row - 1][col - 1][0]
                    + dp[row - 1][col - 1][1]
                    + dp[row - 1][col - 1][2]
                )  # 대각선으로 가기

print(sum(dp[N - 1][N - 1]))
# print(dp)

