import heapq

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dijkstra(graph, row, col):
    count_change_room = [[float("inf") for _ in range(n)] for _ in range(n)]
    count_change_room[row][col] = 0
    heap = []
    heapq.heappush(heap, (0, row, col))

    while heap:
        current_count_change_room, cRow, cCol = heapq.heappop(heap)

        if current_count_change_room > count_change_room[cRow][cCol]:
            continue

        for dRow, dCol in direction:
            nRow = cRow + dRow
            nCol = cCol + dCol
            if not (0 <= nRow < n and 0 <= nCol < n):
                continue

            if count_change_room[nRow][nCol] > current_count_change_room + (1 - graph[nRow][nCol]):
                count_change_room[nRow][nCol] = current_count_change_room + (1 - graph[nRow][nCol])
                heapq.heappush(heap, (count_change_room[nRow][nCol], nRow, nCol))

    return count_change_room


result = 0

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

result = dijkstra(graph, 0, 0)
print(result[n - 1][n - 1])
