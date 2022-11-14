import sys


input = sys.stdin.readline

N, M = map(int, input().split())

givenNumbers = list(map(int, input().split()))
givenNumbers.sort()
visited = [False for _ in range(N)]


def NM(count, numList, idx):
    global N, M
    if count == M:
        print(*numList)
    else:
        for i in range(0, N):
            if i != idx and visited[i] == False:
                numList.append(givenNumbers[i])
                visited[i] = True
                NM(count + 1, numList, i)
                numList.pop()
                visited[i] = False


numList = []
NM(0, numList, -1)
