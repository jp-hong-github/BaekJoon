import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
graph.insert(0, 0)
a, b = map(int, input().split())
visited = [False for _ in range(N + 1)]

result = int(10e9)

q = deque([(a, 0)])

while q:
    current_position, current_step = q.popleft()
    if current_step > result:
        continue
    if visited[current_position] is True:
        continue
    if current_position == b:
        if current_step < result:
            result = current_step
        continue

    visited[current_position] = True
    # 양의 방향으로 이동
    positive = 1
    while current_position + positive * graph[current_position] <= N:
        q.append(
            (current_position + positive * graph[current_position], current_step + 1)
        )
        positive += 1

    # 음의 방향으로 이동
    negative = -1
    while current_position + negative * graph[current_position] > 0:
        q.append(
            (current_position + negative * graph[current_position], current_step + 1)
        )
        negative -= 1

if result != int(10e9):
    print(result)
else:
    print(-1)
