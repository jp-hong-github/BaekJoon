import sys

input = sys.stdin.readline

n, k = map(int, input().split())

from collections import deque

visited = [abs(i - n) for i in range(100001)]  # 오는데 걸린 시간
ways = [0] * 100001  # 최소 시간으로 오는 방법의 수
time = 0
ways[n] = 1

if k <= n:
    print(abs(k - n))
    print(1)
else:
    q = deque()
    q.append(n)
    stop = 0
    # 큐가 빌 때까지 반복
    while q:
        s = len(q)
        for i in range(s):
            current = q.popleft()
            next = [current + 1, current - 1, current * 2]
            for z in next:
                if 0 <= z and z <= 100000 and time + 1 <= visited[z]:
                    ways[z] += 1
                    visited[z] = time + 1
                    if k == z:
                        stop = 1
                    else:
                        q.append(z)
        time += 1
        if stop == 1:
            break

    print(visited[k])
    print(ways[k])
# print(ways[:20])
