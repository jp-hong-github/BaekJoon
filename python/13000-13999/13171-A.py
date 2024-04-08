import sys

input = sys.stdin.readline


def power(base, exponent):
    base %= BIG_NUMBER
    # 지수가 0일 때
    if exponent == 0:
        return 1

    if exponent % 2 == 0:  # 지수가 짝수인 경우
        half = power(base, exponent // 2)
        return half * half % BIG_NUMBER
    else:  # 지수가 홀수인 경우
        half = power(base, (exponent - 1) // 2)
        return base * half * half % BIG_NUMBER


A = int(input())
X = int(input())
BIG_NUMBER = 1000000007

result = power(A, X)


print(result % BIG_NUMBER)
