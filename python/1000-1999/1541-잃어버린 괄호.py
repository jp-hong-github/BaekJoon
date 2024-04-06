import sys

input = sys.stdin.readline

string = input().rstrip()
string_split_minus = string.split("-")

result = 0
for i in range(len(string_split_minus)):
    num = 0
    s_split_plus = string_split_minus[i].split("+")
    for c in s_split_plus:
        num += int(c)
    if i == 0:
        result += num
    else:
        result -= num
print(result)
