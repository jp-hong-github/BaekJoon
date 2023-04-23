import sys

input = sys.stdin.readline

N, M = map(int, input().split())

position_of_gods = [(-1, -1)]
roads = []
for _ in range(N):
    x, y = map(int, input().split())
    position_of_gods.append((x, y))

roads = [[False for __ in range(N + 1)] for _ in range(N + 1)]
connected_roads = []
for _ in range(M):
    a, b = map(int, input().split())
    roads[a][b] = True
    roads[b][a] = True
    connected_roads.append((a, b))


parents = [x for x in range(0, N + 1)]


def find_set(x):
    while x != parents[x]:
        x = parents[x]

    return x


# 이미 연결된 우주신끼리의 그래프
for a, b in connected_roads:
    parents_a = find_set(a)
    parents_b = find_set(b)
    if parents_a > parents_b:
        parents[parents_a] = parents_b
    else:
        parents[parents_b] = parents_a


new_road_candidates = []

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if x == y:
            pass
        if roads[x][y] is True:
            pass
        else:
            dist = ((position_of_gods[x][0] - position_of_gods[y][0]) ** 2 + (position_of_gods[x][1] - position_of_gods[y][1]) ** 2) ** (0.5)
            new_road_candidates.append((x, y, dist))

sum_of_weight = 0
edge_count = 0
new_road_candidates.sort(key=lambda x: x[2])
for x, y, dist in new_road_candidates:
    parent_x = find_set(x)
    parent_y = find_set(y)
    if parent_x != parent_y:
        if parent_x > parent_y:
            parents[parent_x] = parent_y
        else:
            parents[parent_y] = parent_x
        # print(parents)
        # print(x, y, dist)
        sum_of_weight += dist
        edge_count += 1

        if edge_count == N - 1 - M:
            break

print("%.2f" % (sum_of_weight))
