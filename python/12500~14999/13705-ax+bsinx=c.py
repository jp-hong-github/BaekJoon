#부동 소수점을 이용해야 한다.
#실수 오차가 중요하다
import decimal
a,b,c= map(decimal.Decimal,input().split())
import math
decimal.getcontext().prec = 130
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
pi = decimal.Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062')

def sin(x):
    if x> 2*pi:
        x = x % (2*pi)
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s


def f(x):
    return a*x+b*decimal.Decimal(sin(x))-c

left = decimal.Decimal(-1)
right = decimal.Decimal(2000002)

while left <= right:
    mid = (left + right)/decimal.Decimal(2)
    value = f(mid)
    if decimal.Decimal(1.0e-20) > value and decimal.Decimal(-1.0e-20) < value :
        print((round(mid,6)))
        break
    elif value >0:
        right = mid
    else:
        left = mid
    #print(mid)