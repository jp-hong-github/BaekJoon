import sys

input = sys.stdin.readline


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


while True:
    N, M = map(int, input().split())
    result = 0

    if N == 0 and M == 0:
        break

    cd_1 = []
    for _ in range(N):
        cd_1.append(int(input()))

    cd_2 = []
    for _ in range(M):
        cd_2.append(int(input()))

    for i in cd_1:
        if binary_search(cd_2, i) != -1:
            result += 1

    print(result)
