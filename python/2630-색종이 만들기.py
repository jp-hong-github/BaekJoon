import sys

input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

result_0 = 0
result_1 = 0


def cut(x, y, N):
    global result_0
    global result_1
    color = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != graph[i][j]:
                cut(x, y, N // 2)
                cut(x, y + N // 2, N // 2)
                cut(x + N // 2, y, N // 2)
                cut(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result_0 += 1
    else:
        result_1 += 1


cut(0, 0, N)
print(result_0)
print(result_1)
