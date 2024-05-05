import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = [0] + list(map(int, input().split()))

q = deque([i for i in range(1, N + 1)])


for i in range(N):
    cur = q.popleft()

    if i == N - 1:
        print(cur)
        break

    print(cur, end=" ")

    move = arr[cur]
    if move > 0:
        q.rotate(-move + 1)
    else:
        q.rotate(-move)
