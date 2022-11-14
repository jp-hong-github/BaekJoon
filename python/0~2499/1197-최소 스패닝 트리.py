import sys
import heapq
import collections
import sys

# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# V, E = map(int, input().split())

# graph = collections.defaultdict(list)
# visited = [False] * (V + 1)
# for _ in range(E):
#     x, y, weight = map(int, input().split())
#     graph[x].append([weight, x, y])
#     graph[y].append([weight, y, x])


# def prim(graph, start):
#     visited[start] = True
#     candidates = graph[start]
#     heapq.heapify(candidates)
#     # mst = []
#     sum_of_weights = 0

#     while candidates:
#         weight, a, b = heapq.heappop(candidates)
#         if visited[b] == False:
#             visited[b] = True
#             # mst.append((a, b))
#             sum_of_weights += weight

#             for edge in graph[b]:
#                 if visited[edge[2]] == False:
#                     heapq.heappush(candidates, edge)

#     return sum_of_weights


# print(prim(graph, 1))

###############################################################

# 집합의 대표 노드를 찾음
def find_set(x):
    while x != parents[x]:
        x = parents[x]

    return x


input = sys.stdin.readline

V, E = map(int, input().split())
graph = []

for _ in range(E):
    x, y, weight = map(int, input().split())
    graph.append((x, y, weight))

graph.sort(key=lambda x: x[2])
edge_count = 0

parents = [i for i in range(0, V + 1)]
sum_of_weight = 0

for x, y, weight in graph:
    if find_set(x) != find_set(y):  # 각 노드가 속한 집합의 대표 노드가 다를 경우(사이클이 생기지 않을 경우)
        parents[find_set(y)] = find_set(x)  # 유니온 연산
        sum_of_weight += weight
        edge_count += 1

        if edge_count == V - 1:
            break

print(sum_of_weight)
