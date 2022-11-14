import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph =[[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,cost = map(int,input().split())
    graph[x].append((y,cost))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for endPoint in graph[now]:
            cost = dist + endPoint[1]
            if cost < distance[endPoint[0]]:
                distance[endPoint[0]] = cost
                heapq.heappush(q,(cost,endPoint[0]))

start,end = map(int,input().split())
dijkstra(start)
print(distance[end])