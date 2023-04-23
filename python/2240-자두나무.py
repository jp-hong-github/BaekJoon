import sys
input = sys.stdin.readline

t,w = map(int,input().split())
data = [[0] * 31] * 1001
chenge = []

n = int(input())
if n==1:
    data[0][0] = 1
else:
    data[0][1] = 1

for i in range(1,t):
    n = int(input())
    data[i][0] = data[i-1][0]
    
    if n==1 :
        data[i][0]+=1
    for j in range(1,w+1):
        data[i][j] = max(data[i-1][j],data[i-1][j-1])
        if j%2 == n-1:
            data[i][j]+=1


result = -1
for i in range(0,w+1):
    if result < data[t-1][i]:
        result = data[t-1][i]
print(result)