import sys

input = sys.stdin.readline

string = input()

for chr in string:
    if chr.isupper():
        temp = chr.lower()
    else:
        temp = chr.upper()
    print(temp, end="")

