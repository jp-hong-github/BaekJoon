import sys
from collections import deque

input = sys.stdin.readline


# 입력 받기
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부와 최단거리 초기화
visited = [False] * (n + 1)
distance = [0] * (n + 1)


# BFS 구현
def bfs(start):
    queue = deque([start])
    visited[start] = True
    distance[start] = start

    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                distance[y] = distance[x] + 1
                queue.append(y)


# BFS 실행
bfs(start)

# 결과 출력
for i in range(1, n + 1):
    if visited[i]:
        print(distance[i])
    else:
        print(0)
