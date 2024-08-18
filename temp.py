import sys

input = sys.stdin.readline


def rotate(graph, d):
    # 기존의 그래프와 동일한 경우 그대로 반환
    if d == 0:
        return graph
    elif d == 360:
        return graph
    elif d == -360:
        return graph
    else:
        # 90도 회전
        if d == 90:
            return [list(row) for row in zip(*graph[::-1])]
        # 180도 회전
        elif d == 180:
            return [list(row) for row in graph[::-1]][::-1]
        # 270도 회전
        elif d == 270:
            return [list(row) for row in zip(*graph)][::-1]
        # -90도 회전
        elif d == -90:
            return [list(row) for row in zip(*graph)][::-1]
        # -180도 회전
        elif d == -180:
            return [list(row) for row in graph[::-1]][::-1]
        # -270도 회전
        elif d == -270:
            return [list(row) for row in zip(*graph[::-1])]
        else:
            Z


T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    rotated_graph = rotate(graph, d)
    for row in rotated_graph:
        print(*row)


import sys

input = sys.stdin.readline


def rotate(graph, d):
    # 기존의 그래프와 동일한 경우 그대로 반환
    if d == 0:
        return graph
    elif d == 360:
        return graph
    elif d == -360:
        return graph
    else:
        # 45도 회전
        if d == 45 or d == -315:
            return list(zip(*graph[::-1]))
        # 90도 회전
        elif d == 90 or d == -270:
            return list(zip(*graph[::-1]))
        # 135도 회전
        elif d == 135 or d == -225:
            return list(zip(*graph[::-1]))
        # 180도 회전
        elif d == 180 or d == -180:
            return list(zip(*graph[::-1]))
        # 225도 회전
        elif d == 225 or d == -135:
            return list(zip(*graph[::-1]))
        # 270도 회전
        elif d == 270 or d == -90:
            return list(zip(*graph[::-1]))
        # 315도 회전
        elif d == 315 or d == -45:
            return list(zip(*graph[::-1]))
        else:
            return graph


T = int(input())
result = []

for _ in range(T):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result.append(rotate(graph, d))

# TODO : 삭제
print("=========")
for i in result:
    for j in i:
        print(*j)
