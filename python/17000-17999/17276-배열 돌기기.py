import sys

input = sys.stdin.readline


# 반시계방향으로 45도 k번 회전한 그래프 반환
def rotate_counter_clockwise(graph, n, d):

    center = n // 2

    for _ in range(d):
        for j in range(1, n // 2 + 1):
            temp = graph[center - j][center]
            graph[center - j][center] = graph[center - j][center + j]
            graph[center - j][center + j] = graph[center][center + j]
            graph[center][center + j] = graph[center + j][center + j]
            graph[center + j][center + j] = graph[center + j][center]
            graph[center + j][center] = graph[center + j][center - j]
            graph[center + j][center - j] = graph[center][center - j]
            graph[center][center - j] = graph[center - j][center - j]
            graph[center - j][center - j] = temp

    return graph


T = int(input())
result = []

for _ in range(T):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    if d == 0 or d == 360 or d == -360:
        result.append(graph)
        continue
    elif d > 0:
        d = 8 - d // 45
    else:
        d = (-d) // 45

    result.append(rotate_counter_clockwise(graph, n, d))

for i in result:
    for j in i:
        print(*j)
