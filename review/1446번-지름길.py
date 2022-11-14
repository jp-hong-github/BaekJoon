import sys

input = sys.stdin.readline
INF = int(10e9)

n, d = map(int, input().split())

shortcut = []
for _ in range(n):
    start, end, time = map(int, input().split())
    shortcut.append([start, end, time])

distance = [i for i in range(d + 1)]
for i in range(0, d + 1):
    distance[i] = min(distance[i], distance[i - 1] + 1)
    for road in shortcut:
        if i == road[0] and road[1] < d + 1:
            distance[road[1]] = min(distance[road[1]], distance[i] + road[2])

print(distance[d])
