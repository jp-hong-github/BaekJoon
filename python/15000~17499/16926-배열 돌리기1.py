import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def rotation(start, end, graph):
    temp = graph[start[0]][start[1]]
    # 위쪽
    row = start[0]
    for col in range(start[1] + 1, end[1] + 1):
        graph[row][col - 1] = graph[row][col]
    # 오른쪽
    col = end[1]
    for row in range(start[0] + 1, end[0] + 1):
        graph[row - 1][col] = graph[row][col]
    # 아래쪽
    row = end[0]
    for col in range(end[1] - 1, start[1] - 1, -1):
        graph[row][col + 1] = graph[row][col]
    # 왼쪽
    col = start[1]
    for row in range(end[0] - 1, start[0], -1):
        graph[row + 1][col] = graph[row][col]

    graph[start[0] + 1][start[1]] = temp

    if end[0] - start[0] == 1 or end[1] - start[0] == 1:
        pass
    else:
        rotation((start[0] + 1, start[1] + 1), (end[0] - 1, end[1] - 1), graph)


def print_graph(graph):
    for row in graph:
        print(*row)


for _ in range(R):
    rotation((0, 0), (N - 1, M - 1), graph)

print_graph(graph)
