import sys
from collections import deque

input = sys.stdin.readline

graph = []
r, c = map(int, input().split())

for _ in range(r):
    graph.append(list(map(int, input().rstrip())))

dRow = [-1,1,0,0]
dCol = [0,0,-1,1]

def bfs(graph, row, col):
    
    if graph[row][col]==


result = 0
for row in range(r):
    for col in range(c):
        result = bfs(graph, row, col)
print(result)
