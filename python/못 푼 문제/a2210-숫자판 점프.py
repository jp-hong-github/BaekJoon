import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

def dfs(x,y,m,n,graph):
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y,m,n,graph)
        dfs(x+1,y,m,n,graph)
        dfs(x,y-1,m,n,graph)
        dfs(x,y+1,m,n,graph)
        return True
    return False

t= int(input())
result = set([])


graph = []
for i in range(5):
    graph.append(list(map(int,input().split())))

    
result = 0
for i in range(n):
    for k in range(m):
        if dfs(k,i,m,n,graph) == True:
            result+=1
print(result)
