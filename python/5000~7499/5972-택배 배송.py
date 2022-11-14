import sys
input = sys.stdin.readline

n,m =map(int,input().split())

graph = {}

for i in range(m):
    x,y,cost = map(int,input().split())
    if x in graph:
        graph[x].append([y,cost])
    else:
        graph[x] = []
        graph[x].append([y,cost])
    
    if y in graph:
        graph[y].append([x,cost])
    else:
        graph[y] = []
        graph[y].append([x,cost])

#print(graph)

disatnce = [int(10e9)]*(n+1)

import heapq

q = []

heapq.heappush(q,(0,1))
disatnce[1] = 0
while q:
    dist,now = heapq.heappop(q)
    if disatnce[now] < dist:
        continue
    else:
        for road in graph[now]:
            cost = dist + road[1]
            if cost < disatnce[road[0]]:
                disatnce[road[0]] = cost
                heapq.heappush(q,(cost,road[0]))

# print(disatnce)
print(disatnce[n])