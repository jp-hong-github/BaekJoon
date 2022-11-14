import sys
input = sys.stdin.readline

n = int(input())    
graph = {}

#그래프 입력
for i in range(n-1):
    start,end,cost = map(int,input().split())  
    if start in graph:
        graph[start].append((end,cost))
    else:
        graph[start] = [(end,cost)]

print(graph)

#루트노드에서 각 자식 노드로 가는 길 중 가장 긴 것 두개를 고르자
#n=1,2,3+ 일 떄 고려
chooseTwoInThisList = []

def dfs(value):
    

for child in graph[1]:
    # visited = [False] * (n+1)
    # visited[0] = True
    # visited[1] = True
    totalCost = child[1]
    chooseTwoInThisList.append(dfs(child[0]))