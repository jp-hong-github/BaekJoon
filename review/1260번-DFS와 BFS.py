import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, destination = map(int, input().split())
    graph[start].append(destination)
    graph[destination].append(start)


# dfs
def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited, i)


# bfs
def bfs(graph, visited, v):
    q = deque([v])

    visited[v] = True
    while q:
        current = q.popleft()
        print(current, end=" ")
        for next in graph[current]:
            if visited[next] == False:
                visited[next] = True

                q.append(next)
                # print(current, next, q)


# 작은 것을 먼저 방문해야 하므로 정렬
for ele in graph:
    ele.sort()

# print(graph)

# dfs 출력
visited = [False for _ in range(n + 1)]
dfs(graph, visited, v)

print()

# bfs 출력
visited = [False for _ in range(n + 1)]
bfs(graph, visited, v)
