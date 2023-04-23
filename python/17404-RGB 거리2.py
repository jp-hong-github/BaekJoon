import sys
input = sys.stdin.readline

n = int(input())

rgb = []
for i in range(0,n):
    rgb.append(list(map(int,input().split())))


result = int(10e9)
for k in range(3):
    dp = [[0,0,0]]
    # 첫번째 집 색깔을 그냥 정해버리는 것
    dp[0][0] = int(10e9)
    dp[0][1] = int(10e9)
    dp[0][2] = int(10e9)
    dp[0][k] = rgb[0][k]

    for i in range(1,n):
        temp = []
        temp.append(min(rgb[i][0]+dp[i-1][1],rgb[i][0]+dp[i-1][2]))#첫번째
        temp.append(min(rgb[i][1]+dp[i-1][0],rgb[i][1]+dp[i-1][2]))#두번째
        temp.append(min(rgb[i][2]+dp[i-1][0],rgb[i][2]+dp[i-1][1]))#세번째
        dp.append(temp)
    
    for i in range(0,3):
        if i==k:
            continue
        result = min(result,dp[n-1][i]) # 계산을 해놓고 그냥 안뽑는다
    #print(dp)

print(result)
