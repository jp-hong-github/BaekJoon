import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

q = deque()
visited = [False for _ in range(1000001)]

q.append((S, 0))
visited[S] = True


while q:
    cur, count = q.popleft()

    if cur == G:
        print(count)
        sys.exit()

    for next in [cur + U, cur - D]:
        if not (1 <= next <= F):
            continue

        if visited[next]:
            continue

        visited[next] = True
        q.append((next, count + 1))


print("use the stairs")
