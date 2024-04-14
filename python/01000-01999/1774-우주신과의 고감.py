# import sys
# import decimal
# import math
# from decimal import ROUND_DOWN

# input = sys.stdin.readline

# n, m = list(map(int, input().split()))
# got_position = [[]]
# parents = [i for i in range(n + 1)]

# for _ in range(n):
#     x, y = list(map(int, input().split()))
#     x = decimal.Decimal(str(x))
#     y = decimal.Decimal(str(y))

#     got_position.append((x, y))

# graph = []
# for i in range(1, n):
#     for k in range(i, n + 1):
#         weight = (
#             (got_position[i][0] - got_position[k][0]) ** decimal.Decimal("2") + (got_position[i][1] - got_position[k][1]) ** decimal.Decimal("2")
#         ) ** decimal.Decimal("0.5")
#         graph.append((i, k, weight))

# for _ in range(m):
#     a, b = list(map(int, input().split()))
#     if a > b:
#         parents[a] = b
#     else:
#         parents[b] = a


# def find(x):
#     if parents[x] != x:
#         parents[x] = find(parents[x])
#     return parents[x]


# def union(a, b):
#     root_a = find(a)
#     root_b = find(b)
#     if root_a > root_b:
#         parents[root_a] = parents[root_b]
#     elif root_a == root_b:
#         return
#     else:
#         parents[root_b] = parents[root_a]


# def kruskal(graph):
#     edges = sorted(graph, key=lambda x: x[2])
#     mst = []

#     for edge in edges:
#         v1, v2, weight = edge

#         if find(v1) != find(v2):
#             mst.append(edge)
#             union(v1, v2)

#     return mst


# mst = kruskal(graph)
# result = sum([i[2] for i in mst])
# print(result.quantize(decimal.Decimal("0.00"), rounding=ROUND_DOWN))

###########################################################################################
# ! 위의 코드는 논리적으로 같으나 시간 초과가 발생
# Python의 decimal 모듈에서 Decimal 유형을 사용하는 작업은 일반적으로 int 또는 float와 같은 내장 숫자 유형을 사용하는 작업보다 느립니다.

import sys

input = sys.stdin.readline


def calculate_dist(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    parent[max(root_a, root_b)] = min(root_a, root_b)


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

graph = [[]]  # n+1의 개수(인덱스는 0,1 ... n)
for i in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

edges = []  # 1부터 n-1
for i in range(1, n):
    for j in range(i + 1, n + 1):
        edges.append([calculate_dist(graph[i], graph[j]), i, j])
# print(edges)

edges.sort()
result = 0

# mst = []
for edge in edges:
    cost, x, y = edge

    if find(x) != find(y):
        union(x, y)
        result += cost

# print(graph)
# print(edges)
# print(mst)
print("{:.2f}".format(result))
