import sys

input = sys.stdin.readline

s = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(s.find(chr(i)))
