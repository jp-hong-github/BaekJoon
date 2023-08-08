"""
a - f
b - e
c - d
"""
# 면이 하나만 보이는 경우 (n-1)*(n-2)*4 + (n-2)*(n-2) : 가장 작은 수
# 면이 두개만 보이는 경우 (n-1)*4 + (n-2)*4
# 면이 새게 보이는 경우 4

n = int(input())

a, b, c, d, e, f = map(int, input().split())


two = [min(a, f), min(c, d), min(b, e)]
two.sort()
two_s = sum(two[:2])

temp = [a, b, c, d, e, f]
temp.sort()
three = temp[0] + temp[1] + temp[2]

if n != 1:
    result = (
        ((n - 1) * (n - 2) * 4 + (n - 2) * (n - 2)) * min(temp)
        + ((n - 1) * 4 + (n - 2) * 4) * two_s
        + 4 * sum(two)
    )
else:
    result = temp[0] + temp[1] + temp[2] + temp[3] + temp[4]
print(result)
