import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def cal(num):
    two, five = 0, 0

    i = 1
    while 2 ** i <= n:
        two += num // 2 ** i
        i += 1
    k = 1
    while 5 ** k <= n:
        five += num // 5 ** k
        k += 1

    return [two, five]


print(
    min(
        (cal(n)[0] - cal(n - m)[0] - cal(m)[0]), (cal(n)[1] - cal(n - m)[1] - cal(m)[1])
    )
)

