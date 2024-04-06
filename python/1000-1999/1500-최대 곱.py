"""
k<=20
k<=s<=100
"""

import sys

input = sys.stdin.readline
s, k = map(int, input().split())

moks = s // k
namuji = s % k

result = [moks] * k
while namuji > 0:
    for i in range(k):
        result[i] += 1
        namuji -= 1
        if namuji == 0:
            break

gop = 1
for value in result:
    gop *= value
print(gop)
