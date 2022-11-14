#백트래킹
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(map(str, input().split()))
