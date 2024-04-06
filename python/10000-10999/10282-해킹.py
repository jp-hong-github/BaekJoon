import sys
import heapq

input = sys.stdin.readline

t = int(input())

result = []
for _ in range(t):
    n, d, c = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    time = [float("inf") for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = list(map(int, input().split()))
        graph[b].append((a, s))

    h = []
    heapq.heappush(h, (0, c))
    time[c] = 0
    com_infection_set = set([c])

    while h:
        current_time, current_com = heapq.heappop(h)
        for neighbor, time_infection in graph[current_com]:
            next_time = time[current_com] + time_infection
            if time[neighbor] > next_time:
                time[neighbor] = next_time
                heapq.heappush(h, (next_time, neighbor))
                com_infection_set.add(neighbor)

    total_time = 0
    for t in time:
        if t != float("inf"):
            total_time = max(total_time, t)

    result.append((len(com_infection_set), total_time))

for r in result:
    print(*r)
