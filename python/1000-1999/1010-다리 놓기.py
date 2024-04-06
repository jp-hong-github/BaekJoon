# 29C13 29!/13!/(29-13)!
def factorial(n):
    if n == 1 or n == 0:  # n이 1일 때
        return 1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)


num = int(input())
nlist = []
for i in range(num):
    nlist.append([int(x) for x in input().strip().split()])
for i in range(num):
    print(
        factorial(nlist[i][1])
        // factorial(nlist[i][0])
        // factorial(nlist[i][1] - nlist[i][0])
    )  # nCr 계산
# /가 아니라 //를 사용해야 한다

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# 2022 01 16 복습
import sys
import itertools

input = sys.stdin.readline
t = int(input())

"""시간초과"""
# for _ in range(t):
#     n, m = map(int, input().split())
#     print(len(list(itertools.combinations(range(1, m + 1), n))))

for _ in range(t):
    n, m = map(int, input().split())
    result = 1
    for a in range(m - n + 1, m + 1):
        result *= a
    for b in range(1, n + 1):
        result //= b
    print(result)
