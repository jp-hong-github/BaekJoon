import sys

input = sys.stdin.readline

N, M = map(int, input().split())
givenNumbers = list(map(int, input().split()))
givenNumbers.sort()


def dfs(idx, numList, count, givenNumbers):
    global N, M
    if count == M:
        print(*numList)
    else:
        for next in range(idx + 1, N):
            numList.append(givenNumbers[next])
            dfs(next, numList, count + 1, givenNumbers)
            numList.pop()


dfs(-1, [], 0, givenNumbers)

