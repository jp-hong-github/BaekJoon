n = int(input())

import heapq

h = []

temp = []
hs = [[] for i in range(n)]

for i in range(n):
    a = list(map(int,input().split()))
    for k in range(n):
        heapq.heappush(hs[k],-a[k])

for i in range(n):
    item = heapq.heappop(hs[i])
    heapq.heappush(h,(item,i))
del temp
#print(hs)

for i in range(n-1):
    t = heapq.heappop(h)
    #print(-t[0])
    heapq.heappush(h,(heapq.heappop(hs[t[1]]),t[1]))

print(-h[0][0])