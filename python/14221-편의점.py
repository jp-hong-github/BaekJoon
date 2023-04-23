import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]



for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


p,q = map(int,input().split())

house = list(map(int,input().split()))
store = list(map(int,input().split()))

distance = {}
for h in house:
    distance[h] = [INF] * (n+1)

def dijkstra(start_house):
    q = []
    heapq.heappush(q,(0,start_house))
    distance[start_house][start_house] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[start_house][now] < dist:
            continue
        for i in graph[now]:
            #pirnt(dist,)
            cost = dist + i[1]
            if cost <distance[start_house][i[0]]:
                distance[start_house][i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
for h in house:
    dijkstra(h)
    
distnace_temp = INF
result = INF
for h in house:
    for s in store:
        if distance[h][s]<distnace_temp:
            distnace_temp = distance[h][s]
            result = h
        elif distance[h][s]==distnace_temp and h<result:
            result = h
        #print(distance[h][s])
#print(distance)
print(result)