import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

visited = [[False for _ in range(m)] for __ in range(n)]

result = 0
for row in range(n):
    for col in range(m):
        if visited[row][col] is False:
            visited[row][col] = True
            # case of '-'
            if graph[row][col] == "-":
                for nCol in range(col + 1, m):
                    if visited[row][nCol] is False:
                        if graph[row][nCol] == "-":
                            visited[row][nCol] = True
                        else:
                            break
                    else:
                        break
            # case of '|'
            elif graph[row][col] == "|":
                for nRow in range(row + 1, n):
                    if visited[nRow][col] is False:
                        if graph[nRow][col] == "|":
                            visited[nRow][col] = True
                        else:
                            break
                    else:
                        break
            result += 1

print(result)
