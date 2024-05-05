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
    # 인덱스가 0으로 오는 것은 회전 방향에 따라 1의 차이가 남
    if move > 0:
        q.rotate(-move + 1)
    else:
        q.rotate(-move)
