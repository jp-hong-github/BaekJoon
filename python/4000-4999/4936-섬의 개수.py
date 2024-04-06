direction_row = [0, 0, 1, 1, 1, -1, -1, -1]
direction_col = [1, -1, 0, 1, -1, 0, 1, -1]


def dfs(graph, row, col, w, h):
    if row <= -1 or row >= h or col <= -1 or col >= w:
        return False
    if graph[row][col] == 1:
        graph[row][col] = 2
        for i in range(8):
            dfs(graph, row + direction_row[i], col + direction_col[i], w, h)
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for i in range(w):
        for k in range(h):
            if dfs(graph, k, i, w, h):
                result += 1

    print(result)
