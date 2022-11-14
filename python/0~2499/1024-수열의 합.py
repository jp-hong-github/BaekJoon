# 참고한 글 : https://hooongs.tistory.com/334
import sys

input = sys.stdin.readline
N, L = map(int, input().split())

# L*x = N-L*(L+1)/2
while L <= 100:
    right_value = N - L * (L + 1) // 2
    if right_value % L == 0:
        x_temp = right_value // L
        if x_temp >= -1:
            x = x_temp
            result = [x + i for i in range(1, L + 1)]
            print(*result)
            break
    L += 1


if L > 100:
    print(-1)
