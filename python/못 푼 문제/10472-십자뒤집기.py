import sys

input = sys.stdin.readline
p = int(input())

for _ in range(p):
    graph = []
    for __ in range(3):
        graph.append(list(input().rstrip()))
