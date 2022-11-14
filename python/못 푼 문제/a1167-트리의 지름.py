import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

v = int(input())

graph = {}

for i in range(v):
    temp = list(map(int, input().split()))
    temp_list = []
    for u in range(1, len(temp) - 1, 2):
        temp_list.append((temp[u], temp[u + 1]))
    graph[temp[0]] = temp_list


result = 0
import heapq


def dfs(start, visited, count):
    global result
    visited[start] = True
    for i in graph[start]:
        destination, cost = i[0], i[1]
        if visited[destination] is not True:
            if result < count:
                result = count
                print(visited, result)
            dfs(destination, visited, count + cost)


for start in graph:
    print(start)
    visited = [False] * (v + 1)
    count = 0
    dfs(start, visited, count)


print(result)

