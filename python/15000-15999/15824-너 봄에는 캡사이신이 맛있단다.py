import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
result = 0

# 5 2 8 의 경우
# 5 2 : 3
# 5 8 : 3
# 2 8 : 6
# 2 5 8 : 6
# 3 + 3 + 6 + 6 = 18


def power(base, exponent):
    if exponent == 0:
        return 1

    # 분할 정복을 이용한 거듭제곱
    if exponent % 2 == 0:  # 지수가 짝수인 경우
        half = power(base, exponent // 2)
        return half * half % 1000000007
    else:  # 지수가 홀수인 경우
        half = power(base, (exponent - 1) // 2)
        return base * half * half % 1000000007


if n == 1:
    pass
else:
    numbers.sort()
    for i in range(n):
        result += numbers[i] * (power(2, i) - power(2, n - i - 1)) % 1000000007
        result %= 1000000007

print(result % 1000000007)
