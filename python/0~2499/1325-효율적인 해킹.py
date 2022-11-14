import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)

result_list = [0 for _ in range(N + 1)]


def bfs(i: int):
    q = deque([i])
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    score = 0
    while q:
        i = q.popleft()
        for next in graph[i]:
            if visited[next] is False:
                visited[next] = True
                q.append(next)
                score += 1
    return score


result = []
max_computer = 0
for i in range(1, N + 1):
    connected_computer_num = bfs(i)
    if connected_computer_num > max_computer:
        result.clear()
        result.append(i)
        max_computer = connected_computer_num
    elif connected_computer_num == max_computer:
        result.append(i)
    else:
        pass
    # print(i, connected_computer_num, max_computer, result)

result.sort()
print(*(result))
