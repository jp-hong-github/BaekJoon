import sys
import heapq

input = sys.stdin.readline

R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(map(str, input().rstrip())))

words = []
for z in range(R):
    temp = ""
    for i in range(C):
        temp += graph[z][i]
    temp = temp.split("#")
    for case in temp:
        if len(case) > 1:
            heapq.heappush(words, case)

for z in range(C):
    temp = ""
    for i in range(R):
        temp += graph[i][z]
    temp = temp.split("#")
    for case in temp:
        if len(case) > 1:
            heapq.heappush(words, case)

print(words[0])
