import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start,end= map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)


for i in range(1,n+1):
    graph[i].sort()

from collections import deque

def bfs(start):
    q = deque([start])
    
    visited = [False for __ in range(n+1)]
    visited[start]= True
    
    while q:
        cur = q.popleft()
        print(cur,end=' ')
        
        for road in graph[cur]:
            if not visited[road]:
                q.append(road)
                visited[road] = True

dfs_visited = [False for __ in range(n+1)]

def dfs(v):
    dfs_visited[v] = True
    print(v,end=' ')
    
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)

dfs(v)
print()
bfs(v)
