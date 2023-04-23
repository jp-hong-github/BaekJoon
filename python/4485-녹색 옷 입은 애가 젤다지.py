# cSpell:ignore heapq

import sys
input = sys.stdin.readline
import heapq


dRow = [-1,1,0,0]
dCol = [0,0,-1,1]
count = 0

while True:
    n = int(input())
    if n==0:   
        break
    else:
        count+=1
        graph = [list(map(int,input().split())) for _ in range(n)]    
        distance = [[int(10e9) for __ in range(n)] for _ in range(n)]
        
        q=[]
        heapq.heappush(q,(graph[0][0],0,0)) # cost, row, col
        distance[0][0] = graph[0][0]
        while q:
            cost,row,col = heapq.heappop(q)
            for i in range(4):
                nRow = dRow[i] + row
                nCol = dCol[i] + col
                
                if nRow < 0 or nRow>=n or nCol < 0 or nCol >= n:
                    continue
                else:
                    current_cost = graph[nRow][nCol] + cost
                    if current_cost < distance[nRow][nCol]:
                        distance[nRow][nCol] = current_cost
                        heapq.heappush(q,(current_cost,nRow,nCol))
        print("Problem %d: %d"%(count,distance[n-1][n-1]))