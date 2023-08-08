import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(M + 1):
    x, y, weight = map(int, input().split())
    if x == 0 and y == 1:
        pass
    graph.append((x, y, weight))


def kruskal(graph):
    def find_set(x):
        while x != parents[x]:
            x = parents[x]
        return x

    parents = [x for x in range(N + 1)]
    edge_count = 0
    sum_of_weight = 0
    for x, y, weight in graph:
        if find_set(x) != find_set(y):
            parents[find_set(y)] = find_set(x)
            sum_of_weight += 1 - weight
            edge_count += 1

        if edge_count == N:
            break

    return sum_of_weight


graph.sort(key=lambda x: x[2])
best = kruskal(graph)
graph.sort(key=lambda x: -x[2])
worst = kruskal(graph)
print(abs(worst**2 - best**2))
