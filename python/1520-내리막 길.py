#
# & pypy3로 할 시 메모리 초과 발생
# & python3로 제출할 것

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

row, col = list(map(int, input().split()))
graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))

dp = [[-1 for _ in range(col)] for _ in range(row)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(cRow, cCol):
    if cRow == row - 1 and cCol == col - 1:
        return 1
    elif dp[cRow][cCol] != -1:
        return dp[cRow][cCol]
    else:
        result = 0
        for dRow, dCol in direction:
            nRow = cRow + dRow
            nCol = cCol + dCol
            if not (0 <= nRow < row and 0 <= nCol < col):
                continue

            if not (graph[nRow][nCol] < graph[cRow][cCol]):
                continue

            result += dfs(nRow, nCol)

    dp[cRow][cCol] = result
    return result


print(dfs(0, 0))

a = 1

# ! 단순 BFS 알고리즘 동작 시 시간 초과 발생
# ===================================================================================== #
# heap = [(0, 0)]
# direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# result = 0

# while heap:
#     # current_row, current_col
#     cRow, cCol = heapq.heappop(heap)
#     # print(cRow, cCol)

#     if cRow == row - 1 and cCol == col - 1:
#         result += 1
#         continue

#     for dRow, dCol in direction:
#         nRow = cRow + dRow
#         nCol = cCol + dCol
#         if not (0 <= nRow < row and 0 <= nCol < col):
#             continue

#         if graph[nRow][nCol] >= graph[cRow][cCol]:
#             continue

#         heapq.heappush(heap, (nRow, nCol))

# print(result)
# ===================================================================================== #
