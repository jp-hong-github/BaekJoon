import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph.sort()

order = 1

for i in range(N + 1):
    graph[i].sort()


def dfs(cur):
    global order
    for next in graph[cur]:
        if visited[next] == 0:
            order += 1
            visited[next] = order
            dfs(next)


visited[R] = 1
dfs(R)

for i in range(1, N + 1):
    print(visited[i])

# print(graph)
