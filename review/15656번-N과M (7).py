import sys

input = sys.stdin.readline

N, M = map(int, input().split())
givenNumbers = list(map(int, input().split()))
givenNumbers.sort()


def dfs(numList, count, givenNumbers):
    global N, M
    if count == M:
        print(*numList)
    else:
        for next in range(0, N):
            numList.append(givenNumbers[next])
            dfs(numList, count + 1, givenNumbers)
            numList.pop()


dfs([], 0, givenNumbers)
