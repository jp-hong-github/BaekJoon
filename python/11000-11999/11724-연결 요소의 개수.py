import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 채우기
for _ in range(m):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [0 for _ in range(n + 1)]


# dfs 코드
def dfs(graph, visited, v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited, i)


# 계산
result = 0
for i in range(1, n + 1):
    if visited[i] == False:
        dfs(graph, visited, i)
        result += 1

# 결과 출력
print(result)
