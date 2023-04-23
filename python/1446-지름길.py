import sys

input = sys.stdin.readline

n, d = map(int, input().split())
road = {}
for _ in range(n):
    start, end, cost = map(int, input().split())
    if end > d:
        continue
    if start not in road:
        road[start] = {end: cost}
    elif end not in road[start]:
        road[start][end] = cost
    elif end in road[start] and road[start][end] > cost:
        road[start][end] = cost

distance = [i for i in range(d + 1)]
for i in range(0, d + 1):
    distance[i] = min(distance[i], distance[i - 1] + 1)
    if i in road:
        for end in road[i]:
            distance[end] = min(distance[end], distance[i] + road[i][end])

print(distance[d])

