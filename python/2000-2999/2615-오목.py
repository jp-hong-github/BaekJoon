import sys

input = sys.stdin.readline

graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))

visited = [[[False, False, False, False] for __ in range(19)] for _ in range(19)]


d_row = [0, 1, 1, 1]
d_col = [1, 0, 1, -1]

result = {"color_win": None, "row": None, "col": None}


def dfs(graph, first_row, first_col, row, col, direction, color, win_check):
    global result
    if graph[row][col] == 0:
        return
    if visited[row][col][direction]:
        return
    else:
        visited[row][col][direction] = True
        next_row = row + d_row[direction]
        next_col = col + d_col[direction]
        if (
            not (next_row >= 19 or next_col >= 19 or next_row <= -1 or next_col <= -1)
            and graph[next_row][next_col] == color
        ):
            if next_col < first_col:
                first_row = next_row
                first_col = next_col
            dfs(
                graph,
                first_row,
                first_col,
                next_row,
                next_col,
                direction,
                color,
                win_check + 1,
            )
            # print(row, col, win_check)
        else:
            if win_check == 5:
                result["color_win"] = color
                result["row"] = first_row + 1
                result["col"] = first_col + 1


for c_row in range(19):
    for c_col in range(19):
        for direction in range(4):
            dfs(graph, c_row, c_col, c_row, c_col, direction, graph[c_row][c_col], 1)

if result["color_win"] is None:
    print(0)
else:
    print(result["color_win"])
    print(f'{result["row"]} {result["col"]}')
