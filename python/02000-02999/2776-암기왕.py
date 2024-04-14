import sys

input = sys.stdin.readline

T = int(input())  # 테스트 케이스

for _ in range(T):
    N = int(input())
    memo_1 = list(map(int, input().split()))

    M = int(input())
    memo_2 = list(map(int, input().split()))

    memo_1.sort()

    for num in memo_2:
        start = 0
        end = N - 1

        flag = False
        while start <= end:
            mid = (start + end) // 2
            if memo_1[mid] == num:
                flag = True
                break
            elif memo_1[mid] > num:
                end = mid - 1
            else:
                start = mid + 1

        if flag is True:
            print(1)
        else:
            print(0)
