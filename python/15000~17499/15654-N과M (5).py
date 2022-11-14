import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.insert(0,0)
arr.sort()

result = []

def dfs(idx,count):
    if count == m:
        for i in result:
            print(i,end=' ')
        print()
    else:
        for i in range(0, n+1):
            if i!=idx and arr[i]!=0 and arr[i] not in result:
                result.append(arr[i])
                dfs(i, count+1)
                result.pop()
            else:
                continue

dfs(0, 0)