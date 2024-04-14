import sys
from collections import deque

# from collections import Counter

input = sys.stdin.readline


# def find(parents, v):
#     if parents[v] != v:
#         parents[v] = find(parents, parents[v])
#     return parents[v]


# def union(parents, a, b):
#     root_a = find(parents, a)
#     root_b = find(parents, b)
#     if root_a > root_b:
#         parents[root_a] = root_b
#     elif root_a < root_b:
#         parents[root_b] = root_a


# k = int(input())
# for _ in range(k):
#     v, e = map(int, input().split())
#     graph = []
#     for _ in range(e):
#         graph.append(list(map(int, input().split())))

# 아이디어 : MST를 저장하지 않는 크루스칼 알고리즘
# ! 문제를 잘못 이해해서 불가
# parents = [i for i in range(v + 1)]
# for u, v in graph:
#     root_u = find(parents, u)
#     root_v = find(parents, v)

#     if root_v != root_u:
#         union(parents, v, u)

# root_counter = Counter(parents)

k = int(input())
for _ in range(k):
    result = "YES"
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    # ! 정점이 2개인 경우 이분 그래프를 무조건 만들 수 없음
    if v == 2:
        print("NO")
        continue

    # 0은 아직 방문하지 않음
    # 1,2로 정점에 칠해지 색깔을 구분
    visited = [0 for _ in range(v + 1)]
    # ! 비연결 그래프일 때도 생각해 주어야 함
    for start in range(1, v + 1):
        if visited[start] == 0 and result == "YES":
            visited[start] = 1

            q = deque()
            q.append((start, 1))

            while q:
                cPos, cColor = q.popleft()

                if cColor == 1:
                    nColor = 2
                else:
                    nColor = 1

                for neighbor in graph[cPos]:
                    if visited[neighbor] == 0:
                        q.append((neighbor, nColor))
                        visited[neighbor] = nColor
                    elif visited[cPos] == visited[neighbor]:
                        result = "NO"
                        q = []
                        break

    print(result)
