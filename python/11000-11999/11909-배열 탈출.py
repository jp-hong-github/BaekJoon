import sys
import math
import heapq


input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

# (0,0) => (n-1,n-1)

INF = int(10e9)
# cost_list = [[INF for _ in range(n)] for _ in range(n)]

# q = []
# q.append((0, 0, 0))  # cost,row,col
# cost_list[0][0] = 0


# def check_q(row, col, next_row, next_col, cur_cost):
#     cur_pos_num = graph[row][col]
#     next_pos_num = graph[next_row][next_col]
#     next_cost = cur_cost
#     if cur_pos_num <= next_pos_num:
#         next_cost += next_pos_num - cur_pos_num + 1
#     if cost_list[next_row][next_col] > next_cost:
#         cost_list[next_row][next_col] = next_cost
#         heapq.heappush(q, (next_cost, next_row, next_col))


result = 0
# while q:
#     cur_cost, row, col = heapq.heappop(q)
#     if row == n - 1 and col == n - 1:
#         result = cur_cost
#         break
#     elif row == n - 1 and col < n - 1:
#         # check_q(row, col, row, col + 1, cur_cost)
#         next_row = row
#         next_col = col+1
#         cur_pos_num = graph[row][col]
#         next_pos_num = graph[next_row][next_col]
#         next_cost = cur_cost
#         if cur_pos_num <= next_pos_num:
#             next_cost += next_pos_num - cur_pos_num + 1
#         if cost_list[next_row][next_col] > next_cost:
#             cost_list[next_row][next_col] = next_cost
#             heapq.heappush(q, (next_cost, next_row, next_col))

#     elif row < n - 1 and col == n - 1:
#         # check_q(row, col, row + 1, col, cur_cost)
#         next_row = row+1
#         next_col = col
#         cur_pos_num = graph[row][col]
#         next_pos_num = graph[next_row][next_col]
#         next_cost = cur_cost
#         if cur_pos_num <= next_pos_num:
#             next_cost += next_pos_num - cur_pos_num + 1
#         if cost_list[next_row][next_col] > next_cost:
#             cost_list[next_row][next_col] = next_cost
#             heapq.heappush(q, (next_cost, next_row, next_col))
#     elif 0 <= row < n - 1 and 0 <= col < n - 1:
#         for n_row, n_col in [(1, 0), (0, 1)]:
#             # check_q(row, col, row + n_row, col + n_col, cur_cost)
#             next_row = row+1
#             next_col = col
#             cur_pos_num = graph[row][col]
#             next_pos_num = graph[next_row][next_col]
#             next_cost = cur_cost
#             if cur_pos_num <= next_pos_num:
#                 next_cost += next_pos_num - cur_pos_num + 1
#             if cost_list[next_row][next_col] > next_cost:
#                 cost_list[next_row][next_col] = next_cost
#                 heapq.heappush(q, (next_cost, next_row, next_col))

# print(result)
# ! 다익스트라 포기 ! #

INF = int(10e9)
dp = [[0 for _ in range(n)] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if row == 0 and col == 0:
            continue
        elif row == 0:
            if graph[row][col] >= graph[row][col - 1]:
                dp[row][col] = (
                    dp[row][col - 1] + graph[row][col] - graph[row][col - 1] + 1
                )
            else:
                dp[row][col] = dp[row][col - 1]

        elif col == 0:
            if graph[row][col] >= graph[row - 1][col]:
                dp[row][col] = (
                    dp[row - 1][col] + graph[row][col] - graph[row - 1][col] + 1
                )
            else:
                dp[row][col] = dp[row - 1][col]
        else:
            if graph[row][col] >= graph[row][col - 1]:
                cost1 = dp[row][col - 1] + graph[row][col] - graph[row][col - 1] + 1
            else:
                cost1 = dp[row][col - 1]

            if graph[row][col] >= graph[row - 1][col]:
                cost2 = dp[row - 1][col] + graph[row][col] - graph[row - 1][col] + 1
            else:
                cost2 = dp[row - 1][col]

            dp[row][col] = min(cost1, cost2)

print(dp[n - 1][n - 1])
