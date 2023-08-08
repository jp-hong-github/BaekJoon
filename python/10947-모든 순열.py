import sys

input = sys.stdin.readline

N = int(input())


def permutation(value, count, numList):
    global N
    if count == N:
        print(*numList)
    else:
        for i in range(1, N + 1):
            if i != value and i not in numList:
                numList.append(i)
                permutation(i, count + 1, numList)
                numList.pop()


permutation(0, 0, [])
