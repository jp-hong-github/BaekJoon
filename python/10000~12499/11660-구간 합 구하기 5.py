import sys
input = sys.stdin.readline
n,m = map(int,input().split())

#그래프 채우기
graph = [[0 for _ in range(n+1)]]
for i in range(1,n+1):
    temp = list(map(int,input().split()))
    temp.insert(0,0)
    graph.append(temp)
#x1,y1 x2,y2 입력받기
cases = [list(map(int,input().split())) for _ in range(m)]


for i in range(1, n + 1):
    for j in range(1, n):
        graph[i][j + 1] += graph[i][j]

for j in range(1, n + 1):
    for i in range(1, n):
        graph[i + 1][j] += graph[i][j]

for x1,y1,x2,y2 in cases:
    print(graph[x2][y2] - graph[x1 - 1][y2] - graph[x2][y1 - 1] + graph[x1 - 1][y1 - 1])
