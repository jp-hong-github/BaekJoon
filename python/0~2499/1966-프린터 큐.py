import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque([(p, i) for i, p in enumerate(priorities)])

    order = 0

    while queue:
        doc = queue.popleft()

        if any(doc[0] < q[0] for q in queue):
            queue.append(doc)
        else:
            order += 1
            if doc[1] == m:
                print(order)
                break
