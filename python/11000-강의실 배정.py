import sys
input = sys.stdin.readline
n = int(input())

lectures = []

for i in range(n):
    lectures.append(list(map(int,input().split())))
    
import heapq

lectures.sort(key=lambda a: [a[0], a[1]])   

q = []
count=0
#print(lectures)

for study in lectures:
    start, end = study[0],study[1]
    while True:
        if q and q[0][0] <= study[0]:
            heapq.heappop(q)
        else:
            break
        
    heapq.heappush(q,(end,start)) # 종료 시간, 시작 시간 
    if count < len(q):
        count = len(q)
    #print(q)

print(count)


