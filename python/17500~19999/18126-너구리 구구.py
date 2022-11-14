import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

visited = [False] * (N + 1)
dist_list = [-1] * (N + 1)


def dfs(v, current_dist):
    dist_list[v] = current_dist
    visited[v] = True
    for next, dist in graph[v]:
        if visited[next] is False and visited[next] < current_dist + dist:
            dfs(next, current_dist + dist)


dfs(1, 0)


print(max(dist_list))
