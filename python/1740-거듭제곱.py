import sys

input = sys.stdin.readline


n = int(input())
bin_n = bin(n)
str_bin_n = str(bin_n)[2:]


result = 0
for i in range(len(str_bin_n)):
    if str_bin_n[i] == "1":
        result += 3 ** (len(str_bin_n) - 1 - i)

print(result)
