n = int(input())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

dp1_min = [data[0]]

dp1_max = [data[0]]


for i in range(1,n):
    temp_min = []
    temp_min.append(data[i][0]+min(dp1_min[i-1][0],dp1_min[i-1][1]))
    temp_min.append(data[i][1]+min(dp1_min[i-1][0],dp1_min[i-1][1],dp1_min[i-1][2]))
    temp_min.append(data[i][2]+min(dp1_min[i-1][1],dp1_min[i-1][2]))
    dp1_min.append(temp_min)
    
    temp_max = []
    temp_max.append(data[i][0]+max(dp1_max[i-1][0],dp1_max[i-1][1]))
    temp_max.append(data[i][1]+max(dp1_max[i-1][0],dp1_max[i-1][1],dp1_max[i-1][2]))
    temp_max.append(data[i][2]+max(dp1_max[i-1][1],dp1_max[i-1][2]))
    dp1_max.append(temp_max)
    
print("%d %d"%(max(dp1_max[-1]),min(dp1_min[-1])))