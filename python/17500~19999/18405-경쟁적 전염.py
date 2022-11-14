# cSpell:ignore deque

import sys
from collections import deque

input=sys.stdin.readline

n,k = map(int,input().split())

graph = []
virus = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j],0,i,j))


s,target_row,target_col = map(int,input().split())

dCol=[-1,1,0,0]
dRow=[0,0,-1,1]
virus.sort()
q = deque(virus)
    
while q:
    virus_num,current_time,row,col = q.popleft()
    if s == current_time:
        break
    for i in range(4):
        nRow = row + dRow[i]
        nCol = col + dCol[i]
        
        if nRow<0 or nCol<0 or nRow>=n or nCol>=n:
            continue
        else:
            if graph[nRow][nCol] == 0:
                graph[nRow][nCol] = virus_num
                q.append((virus_num,current_time+1,nRow,nCol))
                
print(graph[target_row-1][target_col-1])