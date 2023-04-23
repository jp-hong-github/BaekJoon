import sys
input = sys.stdin.readline
r,c,t = map(int,input().split())

graph = []
air_ = []

for i in range(r):
    temp = list(map(int,input().split()))
    if -1 == temp[0]:
        air_temp = [i,0]
        air_.append(air_temp)
    graph.append(temp)

# 미세먼지가 퍼져나가는 함수
def misemonji():
        visited = [[0 for _ in range(c)] for __ in range(r)]
        for cRow in range(r):
            for cCol in range(c):
                if graph[cRow][cCol] !=0 and graph[cRow][cCol] !=-1 and (cRow,cCol) not in visited: # 미세먼지가 존재하는 경우
                    dRow = [0,0,-1,1]
                    dCol = [-1,1,0,0]
                    for i in range(4):
                        nRow = cRow + dRow[i]
                        nCol = cCol + dCol[i]
                        
                        if nRow>=r or nRow<0 or nCol>=c or nCol<0:
                            continue
                        if graph[nRow][nCol] == -1:
                            continue
                        
                        visited[nRow][nCol] += graph[cRow][cCol]//5
                        visited[cRow][cCol] -= graph[cRow][cCol]//5
                        
        for cRow in range(r):
            for cCol in range(c):
                graph[cRow][cCol] += visited[cRow][cCol]
        del visited

# 공기 청정기에서 바람이 나가는 함수
def air_wind():
    # 위쪽 바람일 경우
    # ex: [0,3]
    upRow = air_[0][0]
    #1
    graph[upRow-1][0] = 0
    for i in range(upRow-2,-1,-1):
        graph[i+1][0] = graph[i][0]
    #2
    for i in range(1,c):
        graph[0][i-1] = graph[0][i]
    #3
    for i in range(1,upRow+1):
        graph[i-1][c-1] = graph[i][c-1]
    #4
    for i in range(c-2,0,-1):
        graph[upRow][i+1] = graph[upRow][i]
    graph[upRow][1] = 0
        
    #아랫쪽 바람일 경우
    #ex: [0,4]
    downRow = air_[1][0]
    #1
    graph[downRow+1][0] = 0
    for i in range(downRow+2,r):
        graph[i-1][0] = graph[i][0]
    #2
    for i in range(1,c):
        graph[r-1][i-1] = graph[r-1][i]
    #3
    for i in range(r-2,downRow-1,-1):
        graph[i+1][c-1] = graph[i][c-1]
    #4
    for i in range(c-2,0,-1):
        graph[downRow][i+1] = graph[downRow][i]
    graph[downRow][1] = 0


for i in range(t):
    # 미세먼지의 확산
    misemonji()
    # 공기 청정기 바람의 확산
    air_wind()
    
# 미세먼지의 양 출력
result = 0
for q in graph:
    for i in q:
        result +=i
        
print(result+2)