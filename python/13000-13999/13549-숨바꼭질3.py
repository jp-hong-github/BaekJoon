import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 다익스트라
import heapq

INF = int(10e9)
distance = [INF for _ in range(100001)]

q = []
heapq.heappush(q, (0, N))
distance[N] = 0
while q:
    # 여기선 dist 보다 time이 더 적절하다고 생각함
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for next in [now - 1, now + 1]:
        if (0 <= next and next <= 100000) and distance[next] > dist + 1:
            distance[next] = dist + 1
            heapq.heappush(q, (dist + 1, next))
            # print(dist + 1, next)

    next = now * 2
    if (0 <= next and next <= 100000) and distance[next] > dist:
        distance[next] = dist
        heapq.heappush(q, (dist, next))
        # print(dist, next)

print(distance[K])

# BFS
from collections import deque

INF = int(10e9)
time = [INF for _ in range(100001)]  # visited보다 그냥 time이 더 나은 듯
q = deque([N])
time[N] = 0

while q:
    current = q.popleft()

    next = current + 1
    if (0 <= next and next <= 100000) and time[next] > time[current] + 1:
        time[next] = time[current] + 1
        q.append(next)

    next = current - 1
    if (0 <= next and next <= 100000) and time[next] > time[current] + 1:
        time[next] = time[current] + 1
        q.append(next)

    next = current * 2
    if (0 <= next and next <= 100000) and time[next] > time[current]:
        time[next] = time[current]
        q.append(next)

print(time[K])
