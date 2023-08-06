import sys

input = sys.stdin.readline

N = int(input())
paths: list = [input().rstrip() for _ in range(N)]
trie = {}


# 경로를 trie에 삽입
def insert_tire(path):
    directories = path.split("\\")
    current = trie
    for dir in directories:
        if dir not in current:
            current[dir] = {}
        current = current[dir]


# 경로를 출력
def print_path(whitespace_count, dir, current_trie):
    print(" " * whitespace_count + dir)
    sorted_sub_dir_keys = sorted(current_trie[dir].keys())
    for sub_dir_key in sorted_sub_dir_keys:
        print_path(whitespace_count + 1, sub_dir_key, current_trie[dir])


# 경로를 트라이에 삽입함
for path in paths:
    insert_tire(path)

sorted_root_dir = sorted(trie.keys())
for root_dir in sorted_root_dir:
    print_path(0, root_dir, trie)
