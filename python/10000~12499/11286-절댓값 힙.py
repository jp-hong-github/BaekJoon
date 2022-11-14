import heapq


n = int(input())

heap = []
result = []

for i in range(n):
    item = int(input())
    if item == 0:
        if len(heap)==0:
            result.append((0,0))
        else:
            result.append(heapq.heappop(heap))
    else:
        if item < 0:
            heapq.heappush(heap,(abs(item),-1))
        else:
            heapq.heappush(heap,(item,1))
            
for i in result:
    if i[0] == 0:
        print(0)
    elif i[1] == -1:
        print(-i[0])
    else:
        print(i[0])