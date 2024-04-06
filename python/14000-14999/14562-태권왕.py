import sys
from collections import deque


input = sys.stdin.readline

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())

    result = int(10e9)
    q = deque([(S, T, 0)])  # 마지막은 현재 발차기를 한 횟수

    while q:
        s, t, value = q.popleft()
        # A
        s_next = s * 2
        t_next = t + 3
        if s_next == t_next:
            result = min(result, value + 1)
        elif s_next > t_next:
            pass
        else:
            q.append([s_next, t_next, value + 1])

        # B
        s_next = s + 1
        t_next = t
        if s_next == t_next:
            result = min(result, value + 1)
        elif s_next > t_next:
            pass
        else:
            q.append((s_next, t_next, value + 1))

    print(result)
