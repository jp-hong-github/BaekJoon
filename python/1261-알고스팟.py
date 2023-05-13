import sys
import heapq
import math

input = sys.stdin.readline
INF = math.inf

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dijkstra(graph, start):
    count_wall_break = [[INF for _ in range(m)] for _ in range(n)]
    sRow, sCol = start
    count_wall_break[sRow][sCol] = 0

    heap = [(0, sRow, sCol)]

    while heap:
        current_count_wall_break, current_row, current_col = heapq.heappop(heap)

        if current_count_wall_break > count_wall_break[current_row][current_col]:
            continue

        for direction_row, direction_col in direction:
            next_row = current_row + direction_row
            next_col = current_col + direction_col

            if not (0 <= next_row < n and 0 <= next_col < m):
                continue

            next__count_wall_break = current_count_wall_break + graph[next_row][next_col]
            if next__count_wall_break < count_wall_break[next_row][next_col]:
                count_wall_break[next_row][next_col] = next__count_wall_break
                heapq.heappush(heap, (next__count_wall_break, next_row, next_col))

    return count_wall_break


#
m, n = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

start_pos = (0, 0)
end_pos = (n - 1, m - 1)
print(dijkstra(graph, start_pos)[end_pos[0]][end_pos[1]])
