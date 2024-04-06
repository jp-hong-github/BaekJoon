import sys
from collections import defaultdict

input = sys.stdin.readline

result = 0
word_set_dict = defaultdict(int)
N = int(input())
for _ in range(N):
    word = tuple(sorted(list(input().rstrip())))
    word_set_dict[word] += 1

print(len(word_set_dict))
