# 20210119 복습
import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()


# 이진탐색
def binary_search_tree(num):
    global A
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == num:
            return True
        elif A[mid] > num:
            end = mid - 1
        else:
            start = mid + 1


for num in B:
    if binary_search_tree(num) is True:
        print(1)
    else:
        print(0)
