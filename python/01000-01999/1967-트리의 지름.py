import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]


def bfs(node, graph, n):
    q = deque([[node, 0]])
    visited = [False for _ in range(n + 1)]
    visited[node] = True
    result_dist = 0
    result_point = None

    while q:
        current, dist = q.popleft()
        for next, cost in graph[current]:
            if visited[next] is False:
                visited[next] = True
                dist_temp = cost + dist
                q.append([next, dist_temp])
                if result_dist < dist_temp:
                    result_dist = dist_temp
                    result_point = next

    return result_dist, result_point


# 그래프 입력
if n == 1:
    print(0)
else:
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    r1, p1 = bfs(1, graph, n)
    answer, p2 = bfs(p1, graph, n)
    print(answer)
