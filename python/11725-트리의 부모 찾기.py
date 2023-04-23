import sys
input = sys.stdin.readline

n = int(input())
graph = {}

for i in range(n-1):
    a,b = map(int,input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

from collections import deque
result = [0] *(n+1)

q = deque([1])
while q:
    value = q.popleft()
    for u in graph[value]:
        result[u] = value
        graph[u].remove(value)
        q.append(u)

for i in range(2,n+1):
    print(result[i])
