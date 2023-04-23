INF = int(1e9)

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
    
for z in range(n):
    for a in range(n):
        for b in range(n):
            #print(z,a,b)
            graph[a][b] = min(graph[a][b],graph[a][z]+graph[z][b])
            
for mm in range(m):
    start,end,cost = map(int,input().split())
    if graph[start-1][end-1] <= cost:
        print("Enjoy other party")
    else:
        print("Stay here")