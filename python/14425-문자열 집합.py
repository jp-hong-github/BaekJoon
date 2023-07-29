import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
result = 0
for _ in range(N):
    S.add(input().rstrip())

for _ in range(M):
    str_to_check = input().rstrip()
    if str_to_check in S:
        result += 1


print(result)
