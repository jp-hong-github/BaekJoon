import sys

input = sys.stdin.readline

N = int(input())
words_list = []

for _ in range(N):
    words_list.append(input().rstrip())

selected_word_set = set()
selected_word_set.add(words_list[0])

word_count = 1
while words_list:
    current_word = words_list.pop()
    is_new_word = True
    for i in range(len(current_word)):
        rotated_current_word = current_word[i:] + current_word[0:i]
        if rotated_current_word in selected_word_set:
            is_new_word = False
            # print(rotated_current_word, selected_word_set)
            break

    if is_new_word:
        selected_word_set.add(current_word)
        word_count += 1

print(word_count)
