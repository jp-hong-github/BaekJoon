import sys
from heapq import heappop, heappush

input = sys.stdin.readline

t = int(input())

results = []
for _ in range(t):
    n, m = list(map(int, input().split()))

    sum_dist = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        graph[a].append((b, c))
        graph[b].append((a, c))

    k = int(input())
    pos_friends = list(map(int, input().split()))

    for pos_friend in pos_friends:
        temp_dist = [float("inf") for _ in range(n + 1)]
        h = []
        temp_dist[pos_friend] = 0
        heappush(h, (0, pos_friend))

        while h:
            current_dist, current_room = heappop(h)

            if current_dist > temp_dist[current_room]:
                continue

            for neighbor_room, neighbor_dist in graph[current_room]:
                temp_sum_dist = neighbor_dist + current_dist
                if temp_sum_dist < temp_dist[neighbor_room]:
                    temp_dist[neighbor_room] = temp_sum_dist
                    heappush(h, (temp_sum_dist, neighbor_room))

        for i, dist in enumerate(temp_dist):
            sum_dist[i] += dist

    min_dist = float("inf")
    min_dist_room = None
    for room, dist in enumerate(sum_dist):
        if min_dist > dist:
            min_dist_room = room
            min_dist = dist

    results.append(min_dist_room)

for result in results:
    print(result)
