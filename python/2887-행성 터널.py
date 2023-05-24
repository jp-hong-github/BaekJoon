import sys

input = sys.stdin.readline

n = int(input())

planets_x = []
planets_y = []
planets_z = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets_x.append((x, i))
    planets_y.append((y, i))
    planets_z.append((z, i))

planets_x.sort()
planets_y.sort()
planets_z.sort()

edges = []
for i in range(n - 1):
    edges.append((abs(planets_x[i][0] - planets_x[i + 1][0]), planets_x[i][1], planets_x[i + 1][1]))
    edges.append((abs(planets_y[i][0] - planets_y[i + 1][0]), planets_y[i][1], planets_y[i + 1][1]))
    edges.append((abs(planets_z[i][0] - planets_z[i + 1][0]), planets_z[i][1], planets_z[i + 1][1]))

parents = [i for i in range(n)]


def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]


def union(a, b):
    A = find(a)
    B = find(b)
    if A > B:
        parents[A] = B
    elif A < B:
        parents[B] = A


result = 0
edges.sort()
for edge in edges:
    weight, u, v = edge

    if find(u) != find(v):
        result += weight
        union(u, v)

print(result)
