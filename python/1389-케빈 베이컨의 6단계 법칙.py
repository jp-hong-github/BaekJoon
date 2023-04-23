INF = int(1e9)
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

result = INF
now = INF
for a in range(1,n+1):
    total = sum(graph[a][1:])
    if now > total:
        if now == total:
            if result > a:
                result = a
                now = total
        else:
            result = a
            now = total
print(result)
#print(graph)