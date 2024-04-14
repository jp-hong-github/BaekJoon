import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

T = int(input())


def dfs(c, r):
    graph[c][r] = "."

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = c + dr, r + dc

        if 0 <= nr < H and 0 <= nc < W and graph[nr][nc] == "#":
            dfs(nr, nc)


for _ in range(T):
    H, W = map(int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(H)]
    result = 0

    for i in range(H):
        for j in range(W):
            if graph[i][j] == "#":
                dfs(i, j)
                result += 1

    print(result)
