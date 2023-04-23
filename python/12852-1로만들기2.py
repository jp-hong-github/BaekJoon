import sys
input = sys.stdin.readline

n = int(input())

import heapq

q=[]

dic = {n:[int(10e8),0]}

heapq.heappush(q,(int(10e9),n,0)) # 방금 지나온 수, 현재 수, 연산 횟수

while q:
    pre,cur,count = heapq.heappop(q)
    if cur <=0:
        continue
    if cur == 1:
        continue
    #print("cur : ",cur,"count : ",count,end=' ')
    if cur%3==0:
        temp = cur//3
        if temp in dic and dic[temp][1] > count+1:
            dic[temp][1] = count+1
            dic[temp][0] = cur
            heapq.heappush(q,(cur,temp,count+1))
        elif temp not in dic:
            dic[temp] = [cur,count+1]
            heapq.heappush(q,(cur,temp,count+1))
        
    if cur%2==0:
        temp = cur//2
        if temp in dic and dic[temp][1] > count+1:
            dic[temp][1] = count+1
            dic[temp][0] = cur
            heapq.heappush(q,(cur,temp,count+1))
        elif temp not in dic:
            dic[temp] = [cur,count+1]
            heapq.heappush(q,(cur,temp,count+1))

    temp = cur - 1
    if temp in dic and dic[temp][1] > count+1:
        dic[temp][1] = count+1
        dic[temp][0] = cur
        heapq.heappush(q,(cur,temp,count+1))
    elif temp not in dic:
        dic[temp] = [cur,count+1]
        heapq.heappush(q,(cur,temp,count+1))
        
    #print("dic : ",dic)


pre=1
print(dic[pre][1])
result = []
while True:
    if pre >= int(10e8):
        break
    result.append(pre)
    pre = dic[pre][0]
    

for i in range(len(result)-1,-1,-1):
    print(result[i],end=' ')