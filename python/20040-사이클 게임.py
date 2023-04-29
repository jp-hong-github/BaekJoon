import sys

input = sys.stdin.readline


# 최상위 부모 노드 찾기
def find_parent(v):
    if v != parents[v]:
        return find_parent(parents[v])
    return v


# 이해하는데 아래의 코드가 더 낫다고 생각
def find_parent2(v):
    if parents[v] == v:
        return v
    else:
        parents[v] = find_parent2(v)
        return parents[v]


# 부모 통합
def union(u, v):
    parent_u = find_parent(u)
    parent_v = find_parent(v)
    if parent_u > parent_v:
        parents[parent_u] = parent_v
    else:
        parents[parent_v] = parent_u


n, m = list(map(int, input().split()))
parents = [i for i in range(n)]
edges = [list(map(int, input().split())) for _ in range(m)]

for idx, edge in enumerate(edges):
    u, v = edge
    if find_parent(u) == find_parent(v):
        print(idx + 1)
        sys.exit()
    else:
        union(u, v)

print(0)
