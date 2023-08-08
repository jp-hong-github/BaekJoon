import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [list(map(str, input().rstrip())) for _ in range(M)]

answer = {"W": 0, "B": 0}


def bfs(row, col, color):
    if color == "V":  # V는 이미 계산되었다는 의미
        return
    else:
        q = deque([[row, col]])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        total = 0
        graph[row][col] = "V"
        printList = []
        while q:
            r, c = q.popleft()

            total += 1
            printList.append([r, c])
            for i in range(4):
                if (0 <= r + dr[i] and r + dr[i] < M) and (
                    0 <= c + dc[i] and c + dc[i] < N
                ):
                    if graph[r + dr[i]][c + dc[i]] == color:
                        q.append([r + dr[i], c + dc[i]])
                        graph[r + dr[i]][c + dc[i]] = "V"
        # print(printList, total ** 2)
        answer[color] += total**2
    pass


for row in range(M):
    for col in range(N):
        bfs(row, col, graph[row][col])


print(answer["W"], answer["B"])
