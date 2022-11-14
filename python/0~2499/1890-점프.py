#
# // BFS와 DP 이용
# ! BFS로 풀면 메모리 초과 발생
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph_dp = [[0 for _ in range(n)] for __ in range(n)]

# (0,0)->(n-1,n-1)
graph_dp[0][0] = 1
for row in range(0, n):
    for col in range(0, n):
        if graph[row][col] == 0 or ((row != 0 or col != 0) and graph_dp[row][col] == 0):
            continue
        if row + graph[row][col] <= n - 1:
            # graph_dp[row + graph[row][col]][col] = max(
            #     graph_dp[row + graph[row][col]][col], graph_dp[row][col]
            # )
            graph_dp[row + graph[row][col]][col] += graph_dp[row][col]

        if col + graph[row][col] <= n - 1:
            # graph_dp[row][col + graph[row][col]] = max(
            #     graph_dp[row][col + graph[row][col]], graph_dp[row][col]
            # )
            graph_dp[row][col + graph[row][col]] += graph_dp[row][col]


print(graph_dp[n - 1][n - 1])

# for i in graph_dp:
#     print(i)
