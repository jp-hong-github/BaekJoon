import sys

input = sys.stdin.readline

n, m = map(int, input().split())

gender = [None] + list(map(str, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

# 크루스칼 알고리즘을 사용
parents = [i for i in range(n + 1)]


def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]


def union(a, b):
    A = find(a)
    B = find(b)
    if A != B:
        if A > B:
            parents[A] = B
        else:
            parents[B] = A


mst = []
temp_result = 0
for u, v, weight in edges:
    # 남초-남초 또는 여초-여초 학교 끼리의 연결일 경우 생략
    if gender[u] == gender[v]:
        continue

    if find(u) != find(v):
        mst.append((u, v, weight))
        temp_result += weight
        union(u, v)

    if len(mst) == n - 1:
        print(temp_result)
        sys.exit()

print(-1)
