import heapq
import sys

input = sys.stdin.readline

n, d = map(int, input().split())

start = 0
graph = [[] for i in range(n + 1)]

INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(n):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
