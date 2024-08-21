import sys

input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# 분모의 최소공배수
lcm_b = lcm(b1, b2)

a1 = a1 * (lcm_b // b1)
a2 = a2 * (lcm_b // b2)

# 분자의 합
a = a1 + a2

# 분자의 합과 분모의 최소공배수의 최대공약수
g = gcd(a, lcm_b)

print(a // g, lcm_b // g)
