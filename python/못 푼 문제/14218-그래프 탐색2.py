from re import M
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    q = deque([(start,0)])
    visited=[False for _ in range(n+1)]
    result=int(10e9)
    while q:
        current,min_num_of_cities_visited = q.popleft()
        for next in graph[current]:
            if next==1:
                result = min(result,min_num_of_cities_visited)
            elif visited[next] is False:
                
            


new_roads = []
q = int(input())
for _ in range(q):
    new_roads.append(list(map(int, input().split())))
