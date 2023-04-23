import sys

input = sys.stdin.readline
N, J, H = map(int, input().split())


def next_number(num, N):
    if N % 2 == 1 and num == N:
        return num // 2 + 1
    elif num % 2 == 1:
        return num // 2 + 1
    else:
        return num // 2


result = -1
round = 1
while N > 1:
    # 만나는 경우
    if (J - H == 1 and J % 2 == 0 and H % 2 == 1) or (H - J == 1 and J % 2 == 1 and H % 2 == 0):
        result = round
        break

    # 다음 라운드 번호 계산
    J = next_number(J, N)
    H = next_number(H, N)

    # print(J, H)

    # 다음 라운드 준비
    if N % 2 == 1:
        N = N // 2 + 1
    else:
        N = N // 2
    round += 1

print(result)
