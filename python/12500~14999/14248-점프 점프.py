import sys

input = sys.stdin.readline
n = int(input())
stones = list(map(int, input().split()))
stones.insert(0, -1)
start = int(input())

from collections import deque

q = deque([start])
visited = [False for _ in range(n + 1)]
visited[start] = True
while q:
    current = q.popleft()
    jump_distance = stones[current]
    for next in [current - jump_distance, current + jump_distance]:
        if (1 <= next and next <= n) and visited[next] is False:
            visited[next] = True
            q.append(next)
print(visited.count(True))
