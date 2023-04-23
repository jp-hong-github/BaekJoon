import sys,heapq
input = sys.stdin.readline

n,m,r = map(int,input().split())

numOfItems = list(map(int,input().split()))
numOfItems.insert(0,0)
INF = int(1e9)

graph = [[INF] * (n+1)for _ in range(n+1)] 

for a in range(1,n+1):
    graph[a][a] = 0

for _ in range(r):
    a,b,cost = map(int,input().split())
    graph[a][b] = cost
    graph[b][a] = cost
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

result = 0
for i in range(1,n+1):
    temp = 0
    for k in range(1,n+1):
        if graph[i][k]<=m:
            temp+=numOfItems[k]
            
    if result < temp:
        result = temp

print(result)
#print(graph)