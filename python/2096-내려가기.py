import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

min_dp = [graph[0][0],graph[0][1],graph[0][2]]
max_dp = [graph[0][0],graph[0][1],graph[0][2]]

for k in range(1,n):
    min_0 = min_dp[0]
    min_1 = min_dp[1]
    min_2 = min_dp[2]
    
    min_dp[0] = graph[k][0] + min(min_0,min_1)
    min_dp[1] = graph[k][1] + min(min_0,min_1,min_2)
    min_dp[2] = graph[k][2] + min(min_2,min_1)
    
    max_0 = max_dp[0]
    max_1 = max_dp[1]
    max_2 = max_dp[2]
    
    max_dp[0] = graph[k][0] + max(max_0,max_1)
    max_dp[1] = graph[k][1] + max(max_0,max_1,max_2)
    max_dp[2] = graph[k][2] + max(max_2,max_1)

print(max(max_dp),min(min_dp))
