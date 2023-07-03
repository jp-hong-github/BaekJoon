import sys
from collections import deque

input = sys.stdin.readline


a, b, n, m = map(int, input().split())

q = deque()
q.append(n)
visited = [float("inf") for _ in range(100001)]
visited[n] = 0

while q:
    cur = q.popleft()

    for next in [cur - 1, cur + 1, cur - a, cur + a, cur - b, cur + b, cur * a, cur * b]:
        if next == m:
            print(visited[cur] + 1)
            sys.exit()

        if not (0 <= next <= 100000):
            continue

        if visited[cur] + 1 >= visited[next]:
            continue

        # print(next)
        visited[next] = visited[cur] + 1
        q.append(next)
