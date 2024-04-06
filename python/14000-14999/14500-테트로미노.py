import sys

input = sys.stdin.readline


n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = 0


def dfs(cRow, cCol, sum_of_value, cnt):
    global result
    if cnt == 4:
        result = max(result, sum_of_value)
        return
    else:
        for dRow, dCol in direction:
            nRow = cRow + dRow
            nCol = cCol + dCol
            if not (0 <= nRow < n and 0 <= nCol < m):
                continue
            if visited[nRow][nCol] == True:
                continue

            if cnt == 2:
                visited[nRow][nCol] = True
                dfs(cRow, cCol, sum_of_value + graph[nRow][nCol], cnt + 1)
                visited[nRow][nCol] = False
            visited[nRow][nCol] = True
            dfs(nRow, nCol, sum_of_value + graph[nRow][nCol], cnt + 1)
            visited[nRow][nCol] = False


for row in range(n):
    for col in range(m):
        visited[row][col] = True
        dfs(row, col, graph[row][col], 1)
        visited[row][col] = False

print(result)

# ! 시간초과
# def back_tracking(cRow, cCol, cnt, visited, sum_of_num):
#     result = 0
#     if cnt == 4:
#         return sum_of_num
#     else:
#         for dRow, dCol in direction:
#             nRow = cRow + dRow
#             nCol = cCol + dCol
#             if not (0 <= nRow < n and 0 <= nCol < m):
#                 continue

#             if visited[nRow][nCol]:
#                 continue

#             visited[nRow][nCol] = True
#             temp_result = back_tracking(nRow, nCol, cnt + 1, visited, sum_of_num + graph[nRow][nCol])
#             if temp_result > result:
#                 # print(temp_result)
#                 # for r in range(n):
#                 #     for c in range(m):
#                 #         if visited[r][c] is True:
#                 #             print(f"({r} {c})", end=",")
#                 # print()
#                 # print()
#                 result = temp_result

#             visited[nRow][nCol] = False

#     return result


# # ㅗ모양 확인
# directions = [[(-1, 0), (0, -1), (0, 1)], [(1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, -1)], [(-1, 0), (1, 0), (0, 1)]]


# def mountain_check(cRow, cCol):
#     result = 0
#     for direction in directions:
#         continue_check = False
#         sum_of_num = graph[cRow][cCol]
#         for dRow, dCol in direction:
#             nRow = cRow + dRow
#             nCol = cCol + dCol
#             if not (0 <= nRow < n and 0 <= nCol < m):
#                 continue_check = True
#                 break

#             sum_of_num += graph[nRow][nCol]

#         if continue_check == True:
#             continue

#         result = max(result, sum_of_num)
#     return result


# result = 0
# for start_row in range(n):
#     for start_col in range(m):
#         visited = [[False for _ in range(m)] for _ in range(n)]
#         visited[start_row][start_col] = True
#         result = max(result, back_tracking(start_row, start_col, 1, visited, graph[start_row][start_col]))
#         result = max(result, mountain_check(start_row, start_col))

# print(result)
