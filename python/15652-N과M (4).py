# from itertools import combinations_with_replacement

# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())

# result = combinations_with_replacement(range(1,n+1),m)

# for i in result:
#     for u in i:
#         print(u,end=' ')
#     print()

n, m = map(int, input().split())
result = []


def dfs(idx, count):
    # print('result:',result,'count:',count)
    if count == m:
        print(*result)
        return
    for i in range(idx, n):
        # print('result:',result,'count:',count,'i:',i)
        result.append(i + 1)
        dfs(i, count + 1)
        result.pop()


dfs(0, 0)
