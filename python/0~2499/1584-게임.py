import sys

input = sys.stdin.readline

graph = [["safe" for _ in range(500)] for __ in range(500)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for col in range(x1, x2 + 1):
        for row in range(y1, y2 + 1):
            graph[row][col] = "danger"

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for col in range(x1, x2 + 1):
        for row in range(y1, y2 + 1):
            graph[row][col] = "death"

for i in graph:
    print(i)
