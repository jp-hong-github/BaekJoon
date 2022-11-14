import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def NM(value, count, numList):
    global N, M
    if count == M:
        print(*numList)
    else:
        for i in range(value, N + 1):
            numList.append(i)
            NM(i, count + 1, numList)
            numList.pop()


numList = []
NM(1, 0, numList)

