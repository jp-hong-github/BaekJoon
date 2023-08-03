import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]
strings_to_check = [input().rstrip() for _ in range(M)]


# 트라이에 문자열을 삽입하는 함수
def insert_trie(trie, s):
    current = trie
    for char in s:
        if char not in current:
            current[char] = {}
        current = current[char]
    # current["end"] = True


# 트라이에 있는 문자열 중 접두사가 있는지 확인하는 하수
def check_string(trie, s):
    current = trie
    for char in s:
        if char not in current:
            return False
        current = current[char]
    return True


trie = {}

# 트라이에 집합 S의 문자열 삽입
for s in S:
    insert_trie(trie, s)

# 접두사 확인
result = 0
for s in strings_to_check:
    if check_string(trie, s):
        result += 1

print(result)
