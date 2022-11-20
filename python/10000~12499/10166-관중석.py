import sys
import math

input = sys.stdin.readline

d1, d2 = map(int, input().split())
seat_list = [[0 for _ in range(2001)] for _ in range(2001)]
result = 0

for d in range(d1, d2 + 1):
    for i in range(1, d + 1):
        gcd = math.gcd(i, d)
        d_g = d // gcd
        i_g = i // gcd
        if seat_list[i_g][d_g] == 0:
            result += 1
            seat_list[i_g][d_g] = 1
            
print(result)
