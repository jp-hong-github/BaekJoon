import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

in_degree = [0 for _ in range(n + 1)]

graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    in_degree[b] += 1
    graph[a].append(b)

q = deque([])
result = []

for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        q.append(i)
        result.append(i)

while q:
    current_node = q.popleft()

    for neighbor in graph[current_node]:
        if in_degree[neighbor] > 0:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
                result.append(neighbor)

print(*result)
# print(graph)
