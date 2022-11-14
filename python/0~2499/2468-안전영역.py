
import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

n =int(input())

grpah = []
max_value = 0
min_value = 101
for q in range(n):
    temp = list(map(int,input().split()))
    grpah.append(temp)
    max_temp = max(temp)
    min_temp = min(temp)
    if max_temp > max_value:
        max_value = max_temp
    if min_temp < min_value:
        min_value = min_temp
        

def dfs(x,y,value,visited):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if grpah[y][x] > value and visited[y][x]==0:
        visited[y][x] = 1
        dfs(x-1,y,value,visited)
        dfs(x+1,y,value,visited)
        dfs(x,y-1,value,visited)
        dfs(x,y+1,value,visited)
        return True
    return False

result = 0
for i in range(min_value-1,max_value):
    val = 0
    visited =[[0 for _ in range(n)] for __ in range(n)]
    for k in range(n):
        for j in range(n):
            if dfs(k,j,i+0.5,visited) == True:
                val+=1
    #print(val)
    if result < val:
        result = val

print(result)
