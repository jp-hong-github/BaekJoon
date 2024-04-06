import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

tree = [{} for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, cost = map(int, input().split())
    tree[x][y] = cost
    tree[y][x] = cost


def bfs(a, b):
    queue = deque([[a, 0]])  # 현재 위치, 이동 길이
    visited = [False for _ in range(N + 1)]
    visited[a] = True
    answer = int(10e9)
    while queue:
        current, move = queue.popleft()
        if current == b:
            answer = min(answer, move)
        else:
            for next in tree[current]:
                if not visited[next]:
                    queue.append([next, move + tree[current][next]])
                    visited[next] = True
    return answer


for _ in range(M):
    alpha, beta = map(int, input().split())
    result = bfs(alpha, beta)
    print(result)
