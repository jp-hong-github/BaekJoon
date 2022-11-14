import sys

input = sys.stdin.readline
n, k = map(int, input().split())

# 1~9 : 9
# 10~99 : 90*2 = 180
# 100~999 : 900*3 = 2700
# N = 123456 len=6
# 9*(10**(1-1))*1 + 9*(10**(2-1))*2 + 9*(10**(3-1))*3 + 9*(10**(4-1))*4 + 9*(10**(5-1))*5

ans = 0
digit = 1
nine = 9


while k > digit * nine:
    k = k - (digit * nine)
    ans = ans + nine
    digit += 1
    nine = nine * 10

ans = (ans + 1) + (k - 1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k - 1) % digit])

