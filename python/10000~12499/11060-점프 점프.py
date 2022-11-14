import sys

input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
dp = [int(10e9) for _ in range(N)]
from collections import deque

q = deque([])
q.append((0, 0))  # 현재 위치. 이동 횟수

while q:
    current_pos, move_count = q.popleft()
    if current_pos >= N:
        continue
    if current_pos == N - 1:
        dp[N - 1] = min(dp[N - 1], move_count)
        continue
    for next_move in range(1, graph[current_pos] + 1):
        if current_pos + next_move < N and move_count + 1 < dp[current_pos + next_move]:
            dp[current_pos + next_move] = move_count + 1
            q.append((current_pos + next_move, move_count + 1))


if dp[N - 1] == int(10e9):
    print(-1)
else:
    print(dp[N - 1])
