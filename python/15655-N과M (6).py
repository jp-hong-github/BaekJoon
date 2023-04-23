import sys
input = sys.stdin.readline
n,m = map(int,input().split())
sys.setrecursionlimit(10000)
arr = list(map(int,input().split()))
#arr.insert(0,0)
arr.sort()

result = []
def dfs(idx,count):
    if count == m:
        for u in result:
            print(u,end =' ')
        print()
    else:
        for i in range(idx+1,n,1):
            #print("i:",i,"idx+1:",idx+1,"n:",n,"count:",count)
            result.append(arr[i])
            dfs(i,count+1)
            result.pop()
    #print("Dfs")
dfs(-1,0)