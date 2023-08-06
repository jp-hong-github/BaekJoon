import sys

input = sys.stdin.readline

Q = int(input())
queries = [input().rstrip() for _ in range(Q)]

trie_A = {}
trie_B = {}

# add 쿼리 함수
def operate_add_query(trie,s):
    current = trie
    for c in s:
        if c in current:
            current[c] = {}
        current = current[c]
    # 문자열의 마지막을 표시
    current['!'] = True 

# delete 쿼리 함수
def operate_delete_query(trie,s):
    pass

# find 쿼리 함수
def operate_find_query(s):
    pass

for q in queries:
    
