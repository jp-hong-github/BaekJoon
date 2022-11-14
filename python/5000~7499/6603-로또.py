import sys

input = sys.stdin.readline


def backtracking(idx, count, numList, testCase, k):
    if count == 6:
        print(*numList)
    else:
        for i in range(idx + 1, k):
            if testCase[i] not in numList:
                numList.append(testCase[i])
                backtracking(i, count + 1, numList, testCase,k)
                numList.pop()


while True:
    testCase = list(map(int, input().split()))
    if testCase[0] == 0:
        break
    k = testCase[0]  # k만 따로 빼놓기
    del testCase[0]
    backtracking(-1, 0, [], testCase, k)
    print()

