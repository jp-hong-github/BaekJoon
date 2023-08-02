import sys

input = sys.stdin.readline


# 트라이 삽입 함수
def insert(trie, word):
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
    current["is_end_of_word"] = True


# 트라이 조회 함수
def check_include(trie, word):
    current = trie
    for idx, char in enumerate(word):
        # 마지막 단어가 아니면서 문자열의 끝인 경우
        if idx != len(word) and "is_end_of_word" in current:
            return False
        current = current[char]

    if "is_end_of_word" in current:
        return True


t = int(input())
for _ in range(t):
    trie = {}
    n = int(input())
    words = []

    # 트라이에 문자열을 삽입
    for _ in range(n):
        word = input().rstrip()
        words.append(word)
        insert(trie, word)

    # 트라이에서 일관성이 있는 목록인지 확인
    result = "YES"
    for word in words:
        if check_include(trie, word):
            continue
        else:
            result = "NO"
            break

    print(result)
