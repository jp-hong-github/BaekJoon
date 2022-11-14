#부동 소수점을 이용해야 한다.
import decimal
a,b,c= map(decimal.Decimal,input().split())
import math
decimal.getcontext().prec = 130
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
    return a*x+b*sin(x)-c

left = decimal.Decimal(0.0)
right = decimal.Decimal(2000002.0)

while left <= right:
    mid = (left + right)/decimal.Decimal(2.0)
    value = f(mid)
    if decimal.Decimal(1.0e-15) > value and decimal.Decimal(-1.0e-15) < value :
        print("%.19f"%(mid))
        break
    elif value >0:
        right = mid
    else:
        left = mid
    #print(mid)