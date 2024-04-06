from collections import deque
import sys

input = sys.stdin.readline

v = int(input())

tree = [[] for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    index = temp[0]
    if temp[1] == -1:
        continue
    for i in range(1, len(temp), 2):
        if temp[i] == -1:
            continue
        tree[index].append((temp[i], temp[i + 1]))

for i in range(1, v + 1):
    if tree[i]:
        start_node = i
        break


def BFS_looking_for_the_furthest_node(tree, node):
    visited = [False for _ in range(v + 1)]
    visited[node] = True
    q = deque([(node, 0)])  # 두 번째 원소는 거리
    result_distance = 0
    result_node = None

    while q:
        cNode, cDistance = q.popleft()
        if result_distance < cDistance:
            result_node = cNode
            result_distance = cDistance

        for neighbor, distance in tree[cNode]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                q.append((neighbor, cDistance + distance))

    return (result_node, result_distance)


node, _ = BFS_looking_for_the_furthest_node(tree, 1)
_, result = BFS_looking_for_the_furthest_node(tree, node)

print(result)
