import sys

input = sys.stdin.readline


han_su_list = [i for i in range(1, 100)]

for i in range(100, 1001):
    temp = [int(a) for a in str(i)]
    check = True
    for idx in range(len(temp) - 2):
        if temp[idx + 1] - temp[idx] == temp[idx + 2] - temp[idx + 1]:
            pass
        else:
            check = False

    if check:
        han_su_list.append(i)

n = int(input())

result = 0
for i in han_su_list:
    if i <= n:
        result += 1

print(result)
