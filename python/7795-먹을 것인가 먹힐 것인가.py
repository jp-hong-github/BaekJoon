import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    # 이분 탐색을 사용하지 않는 풀이
    A_idx = 0
    B_idx = 0
    result = 0
    dp = 0
    for a in A:
        result += B_idx
        B_idx_temp = B_idx
        for i in range(B_idx_temp, M):
            if B[i] < a:
                result += 1
                B_idx += 1
            if B[i] >= a:
                break

    print(result)
