import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
numbers: list = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

case = list(permutations(numbers[:4], 2))

case_number = [int(str(a) + str(b)) for a, b in case]
case_number.sort()
print(case_number[2])
