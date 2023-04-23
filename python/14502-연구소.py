import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
cases = [(i,k) for i in range(n) for k in range(m)]

virus = [] # 바이러스 위치 저장
for i in range(n):
    for k in range(m):
        if graph[i][k] == 2: # 바이러스
            virus.append([i,k])
            cases.remove((i,k))
        if graph[i][k] == 1: # 벽
            cases.remove((i,k))
            
from itertools import combinations
comb = list(combinations(cases,3))

# for q in virus:
#     print(q)
    
# for q in cases:
#     print(q)

# z=0
# for q in comb:
#     print(q)
#     z+=1
#     if z>30:
#         break

#바이러스 퍼뜨리기 초기에는 2가 들어오고 나중에는 0이 들어온다고 하자
def dfs(temp,row,col):
    dRow = [-1,1,0,0]
    dCol = [0,0,-1,1]
    temp[row][col] = 2 #초기는 어차피 2니까 상관 X
    for i in range(4):
        nRow = dRow[i] + row
        nCol = dCol[i] + col
        if nRow<0 or nCol<0 or nRow>=n or nCol>=m:
            continue
        if temp[nRow][nCol] == 2 or temp[nRow][nCol] == 1:
            continue
        else:
            dfs(temp,nRow,nCol)

temp=[]
result = 0
for first,second,third in comb:
    temp = [graph[i][:] for i in range(n)]
    temp[first[0]][first[1]] = 1
    temp[second[0]][second[1]] = 1
    temp[third[0]][third[1]] = 1
    for vRow,vCol in virus:
        dfs(temp,vRow,vCol)
    
    temp_result = 0
    #print("before count temp : ",temp_result)
    for i in range(n):
        for k in  range(m):
            if temp[i][k]==0:
                temp_result += 1
    # for q in temp:
    #     print(q)
    #print("after count tem : ",temp_result)
    result = max(result,temp_result)
    
print(result)