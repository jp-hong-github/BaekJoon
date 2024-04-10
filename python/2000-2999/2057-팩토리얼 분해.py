import math
import sys

input = sys.stdin.readline

N = int(input())
# 20! = 2432902008176640000이고
# 입력의 최댓값은 1000000000000000000이므로
# 20!까지의 팩토리얼까지만 계산해도 충분함
factorial_lst = [math.factorial(i) for i in range(0, 21)]


def calculate(sum, k):
    # 게산에서 애초에 0!을 제외하고 계산하기 때문에
    # sum에서 1을 더해주었을 때도 확인함
    if sum != 0 and (sum == N or sum + 1 == N):
        print("YES")
        sys.exit()
    elif sum > N:
        return
    else:
        for i in range(k + 1, 21):
            calculate(sum + factorial_lst[i], i)


for i in range(0, 21):
    calculate(0, i)

print("NO")
