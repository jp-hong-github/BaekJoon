# n = int(input())
# import math
# g = 9.81 # 중력가속도

# #f(x)
# def fl(l,v0,H,p):
#     return -(g/2) * (l / v0)**2 + H + p

# #f`(x)
# def fpl(l, v0):
#     return ((-1) * g * l) / v0**2

# #h(x)
# def hl(l,H,L):
#     if l<0:
#         return H
#     elif l<L/2:
#         return H*(1-(2*l**2)/L**2)
#     elif l<L:
#         return 2*H*(l/L-1)**2
#     else:
#         return 0

# #h`(x)
# def hpl(l,H,L):
#     if l<0:
#         return 0
#     elif l<L/2:
#         return -4*H*l/L**2
#     elif l<L:
#         return 4*H*(l/L-1)/L
#     else:
#         return 0
    
# for i in range(n):
#     j,p,H,L = map(int,input().split())
    
#     #초기 속력
#     v0 = math.sqrt(2 * g * j)
    
#     start = 0
#     end = 503
#     while end - start > 1e-10:
#         m = (start + end)/2
#         f = fl(m,v0,H,p)
#         h = hl(m,H,L)
#         if h < f:
#             start = m
#         else:
#             end = m
        
#     l=end
#     hp_l = hpl(l,H,L)
    
#     #착륙 속도(정답임)
#     V = math.sqrt(2*g*(H+p+j-fl(l,v0,H,p)))

#     #언덕에 대한 각도(정답임)
#     fp_l = -g*l/v0**2
#     tan = math.fabs((hp_l-fp_l)/(1+hp_l*fp_l))
#     angle = (math.atan(tan) * 180) / math.pi
    
#     print("%.8f" % l, "%.8f" % V, "%.8f" % angle)

#################################################################
# 걍 맞음

import sys

input = sys.stdin.readline

g = 9.81

test_case = int(input())


def f(x, v0, H, p):
    return ((-0.5) * g * x * x) / (v0 * v0) + H + p


def h(x, H, L):
    if x < 0:
        return H
    elif x < (L / 2):
        return H * (1 - (2 * x * x) / (L * L))
    elif x < L:
        return 2 * H * (x / L - 1) * (x / L - 1)
    else:
        return 0


def f_prime(x, v0):
    return ((-1) * g * x) / (v0 * v0)


def h_prime(x, H, L):
    if x < 0:
        return 0
    elif x < (L / 2):
        return (H * (-4) * x) / (L * L)
    elif x < L:
        return (4 * H * (x / L - 1)) / L
    else:
        return 0

import math
for _ in range(test_case):
    j, p, H, L = map(int, input().split())
    v0 = math.sqrt(2 * g * j)

    end = 0
    high = 500 + 1
    while high - end > 1e-8:						#(1) 착륙 위치(l)
        mid = (high + end) / 2
        if h(mid, H, L) < f(mid, v0, H, p):
            end = mid
        else:
            high = mid

    x = high
    y = f(x, v0, H, p)

    vl = math.sqrt(2 * g * (j + p + H - y))				#(2) 착륙 속도(vl)
    degree = math.atan(math.fabs((h_prime(x, H, L) - f_prime(x, v0)) / (1 + h_prime(x, H, L) * f_prime(x, v0))))
    degree = (degree * 180) / math.pi					#(3) 각도(a)
    print("%.8f" % x, "%.8f" % vl, "%.8f" % degree)
