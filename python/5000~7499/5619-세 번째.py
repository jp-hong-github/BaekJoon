import sys
import heapq

input = sys.stdin.readline

n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))
num_list.sort()


q = []
for i in range(n):
    for k in range(n):
        if i != k:
            heapq.heappush(q, -int("%d%d" % (num_list[i], num_list[k])))
            if len(q) >= 4:
                heapq.heappop(q)


print(-heapq.heappop(q))
