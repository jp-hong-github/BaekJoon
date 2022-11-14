import sys
import heapq

# 다익스트라

input = sys.stdin.readline

N, K = map(int, input().split())

INF = int(10e9)
time_and_post_point = [[INF, INF] for _ in range(100001)]
time_and_post_point[N] = [0, -1]

q = []
heapq.heappush(q, (0, N))

while q:
    time, current = heapq.heappop(q)
    cost = time_and_post_point[current][0] + 1
    for next in [current - 1, current + 1, current * 2]:
        if (0 <= next and next <= 100000) and (time_and_post_point[next][0] > cost):
            time_and_post_point[next] = [cost, current]
            heapq.heappush(q, (cost, next))

point = K
print(time_and_post_point[K][0])
path = []
while True:
    path.insert(0, point)
    if point == N:
        break
    point = time_and_post_point[point][1]

print(*path)
