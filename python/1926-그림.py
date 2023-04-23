import sys
from collections import deque

input = sys.stdin.readline

row, col = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(row)]


def bfs(r, c):
    q = deque([(r, c)])
    graph[r][c] = -1
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    one_count = 0

    while q:
        cur_row, cur_col = q.popleft()

        one_count += 1
        for d_row, d_col in direction:
            if 0 <= cur_row + d_row < row and 0 <= cur_col + d_col < col:
                if graph[cur_row + d_row][cur_col + d_col] == 1:
                    q.append((cur_row + d_row, cur_col + d_col))
                    graph[cur_row + d_row][cur_col + d_col] = -1

    global result_large
    result_large = max(result_large, one_count)


result_large = 0
result_total = 0
for r in range(row):
    for c in range(col):
        if graph[r][c] == 1:
            bfs(r, c)
            result_total += 1
print(result_total)
print(result_large)
