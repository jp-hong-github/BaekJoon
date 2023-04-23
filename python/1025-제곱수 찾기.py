import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

result = -1
for row in range(N):
    for col in range(M):
        for d_row in range(-N, N):
            for d_col in range(-M, M):
                num = graph[row][col]
                n_row = row
                n_col = col
                while True:
                    # print(num)
                    if d_row == 0 and d_col == 0:
                        break
                    n_row = n_row + d_row
                    n_col = n_col + d_col
                    if int(num ** 0.5) ** 2 == num:
                            result = max(result, num)
                    if 0 <= n_row < N and 0 <= n_col < M:
                        num = num * 10 + graph[n_row][n_col]
                    else:
                        break

print(result)
