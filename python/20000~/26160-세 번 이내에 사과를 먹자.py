import sys

input = sys.stdin.readline


graph = []
for i in range(5):
    graph.append(list(map(int, input().split())))

sr, sc = map(int, input().split())


def dfs(r, c, cnt, apple):
    if cnt == 3 or apple >= 2:
        return apple >= 2

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
            continue
        if graph[nr][nc] == -1:
            continue
        temp = graph[nr][nc]
        graph[nr][nc] = -1
        if dfs(nr, nc, cnt + 1, apple + temp):
            return True
        graph[nr][nc] = temp

    return False


graph[sr][sc] = -1
if dfs(sr, sc, 0, 0):
    print(1)
else:
    print(0)
