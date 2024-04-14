import sys

input = sys.stdin.readline

n, k = map(int, input().split())

from collections import deque

q = deque([(n, 0)])
visited = [False for _ in range(100001)]

result = 100001
while q:
    current, value = q.popleft()
    if current < 0 or current > 100000:
        continue
    if visited[current] == True:
        continue
    if current == k:
        result = min(value, result)
    visited[current] = True
    q.append((current + 1, value + 1))
    q.append((current - 1, value + 1))
    q.append((current * 2, value + 1))

print(result)
