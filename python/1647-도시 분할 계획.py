import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(M):
    x, y, weight = map(int, input().split())
    graph.append((x, y, weight))

parents = [x for x in range(0, N + 1)]

graph.sort(key=lambda x: x[2])


def find_set(x):
    while x != parents[x]:
        x = parents[x]
    return x


edge_count = 0
sum_of_weight = 0

for x, y, weight in graph:
    parent_x = find_set(x)
    parent_y = find_set(y)
    if parent_x != parent_y:
        if parent_x > parent_y:
            parents[parent_x] = parent_y
        else:
            parents[parent_y] = parent_x

        sum_of_weight += weight
        edge_count += 1
        if edge_count == N - 2:
            break

print(sum_of_weight)
