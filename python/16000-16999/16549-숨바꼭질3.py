# 13549로 변경됨

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

from collections import deque

visited = [abs(i - n) for i in range(100001)]  # 오는데 걸린 시간
time = 0

if k <= n:
    print(abs(k - n))
else:
    q = deque()
    q.append([n, 0])
    stop = 0
    # 큐가 빌 때까지 반복
    while q:
        s = len(q)
        for i in range(s):
            current, current_time = q.popleft()
            # print(current)
            next = [current + 1, current - 1]
            for z in next:
                if 0 <= z and z <= 100000 and current_time + 1 <= visited[z]:
                    visited[z] = current_time + 1
                    if k == z:
                        stop = 1
                    else:
                        q.append([z, current_time + 1])

            c2 = current * 2
            if 0 <= c2 and c2 <= 100000 and current_time <= visited[c2]:
                visited[c2] = current_time
                if k == c2:
                    stop = 1
                else:
                    q.append([c2, current_time])

        if stop == 1:
            break

    print(visited[k])
# print(ways[:20])
