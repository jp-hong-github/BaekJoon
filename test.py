# 해당 소스 코드가 더 직관적이다.

import heapq
import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 그래프 초기화
n, m = map(int,input().split()) 
graph = collections.defaultdict(list) 
visited = [False] * (n+1) 

for i in range(m):
    x, y, weight = map(int,input().split())
    graph[x].append([weight, x, y])
    graph[y].append([weight, y, x])


def prim(graph, start_node):
    visited[start_node] = True
    candidate = graph[start_node] 
    heapq.heapify(candidate) 
    mst = []
    total_weight = 0 

    while candidate:
        weight, u, v = heapq.heappop(candidate) 
        if visited[v] == False: # 방문한 노드가 아닌 경우
            visited[v] = True
            mst.append((u,v))
            total_weight += weight 

            for edge in graph[v]: # 해당 노드의 간선 서치
                if visited[edge[2]] == False: 
                    heapq.heappush(candidate, edge)

    return total_weight

print(prim(graph,1))