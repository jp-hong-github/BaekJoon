import sys
from collections import defaultdict
from itertools import permutations

input = sys.stdin.readline

name = input().rstrip()

alphabet_dict = defaultdict(int)
for c in name:
    alphabet_dict[c] += 1

if len(name) % 2 == 0:  # 모든 요소가 짝수개여야 함
    for c in alphabet_dict.values():
        if c % 2 != 0:
            print("I'm Sorry Hansoo")
            sys.exit()

    result = []
    for c in alphabet_dict:
        for i in range(alphabet_dict[c] // 2):
            result.append(c)

    result.sort()
    print("".join(result) + "".join(result)[::-1])
else:  # 한개의 요소가 홀수개이고 나머지는 전부 짝수개여야 함
    odd_char = None
    for ch, num in alphabet_dict.items():
        if num % 2 != 0:
            if odd_char is None:
                odd_char = ch
            else:
                print("I'm Sorry Hansoo")
                sys.exit()

    if odd_char is None:  # 홀수인 요소가 한 개도 없는 경우
        print("I'm Sorry Hansoo")
        sys.exit()
    result = []
    for c in alphabet_dict:
        for i in range(alphabet_dict[c] // 2):
            result.append(c)
    result.sort()
    print("".join(result) + odd_char + "".join(result)[::-1])
