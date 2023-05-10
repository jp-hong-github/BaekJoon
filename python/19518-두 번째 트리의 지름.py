import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, cost = list(map(int, input().split()))
    tree[a].append((b, cost))
    tree[b].append((a, cost))

# 트리의 지름을 이루는 정점을 a,b라고 하자
# 트리에서 a를 빼고 지름을 구함
# 트리에서 b를 뺴고 지름을 구함
# 트리에서 a,b를 빼고 지름을 구함

for i in range(1, n + 1):
    if tree[i]:
        start_node = i
        break


def BFS_looking_for_the_furthest_node(tree, node, exclude_node_list=[]):
    visited = [False for _ in range(n + 1)]
    visited[node] = True
    q = deque([(node, 0)])  # 두 번째 원소는 거리
    result_distance = -1
    result_node = None

    while q:
        cNode, cDistance = q.popleft()
        if result_distance < cDistance:
            result_node = cNode
            result_distance = cDistance

        for neighbor, distance in tree[cNode]:
            if visited[neighbor] == False and neighbor not in exclude_node_list:
                visited[neighbor] = True
                q.append((neighbor, cDistance + distance))

    return (result_node, result_distance)


result = 0

# 먼저 트리의 지름을 구함
node_a, _ = BFS_looking_for_the_furthest_node(tree, 1)
node_b, diameter_of_tree = BFS_looking_for_the_furthest_node(tree, node_a)

# a를 제거한 트리의 지름을 구함
node, _ = BFS_looking_for_the_furthest_node(tree, 1, [node_a])
_, second_diameter_of_tree = BFS_looking_for_the_furthest_node(tree, node, [node_a])
result = max(result, second_diameter_of_tree)


# b를 제거한 트리의 지름을 구함
node, _ = BFS_looking_for_the_furthest_node(tree, 1, [node_b])
_, second_diameter_of_tree = BFS_looking_for_the_furthest_node(tree, node, [node_b])
result = max(result, second_diameter_of_tree)

# a,b를 제거한 트리의 지름을 구함
node, _ = BFS_looking_for_the_furthest_node(tree, 1, [node_a, node_b])
_, second_diameter_of_tree = BFS_looking_for_the_furthest_node(tree, node, [node_a, node_b])
result = max(result, second_diameter_of_tree)

print(result)
