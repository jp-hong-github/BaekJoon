import sys
import operator

input = sys.stdin.readline

N = int(input())
alpha_list = []
for _ in range(N):
    alpha_list.append(input().rstrip())


char_dict = {}
for string in alpha_list:
    for i in range(len(string)):
        if string[i] not in char_dict:
            char_dict[string[i]] = 0
        char_dict[string[i]] += 10 ** (len(string) - i - 1)

char_dict_descending_order = sorted(
    char_dict.items(), key=operator.itemgetter(1), reverse=True
)
# print(char_dict_descending_order)

num_dict = {}
num = 9
for c, _ in char_dict_descending_order:
    num_dict[c] = num
    num -= 1
# print(num_dict)

result = 0
for string in alpha_list:
    temp = 0
    for c in string:
        temp += num_dict[c]
        temp *= 10
    result += temp
print(result // 10)
# result = 0
# char_set = set()
# # 어떤 글자들이 있는지 먼저 파악
# for string in alpha_list:
#     for c in string:
#         char_set.add(c)
# char_list = list(char_set)
# permutation_cases = list(
#     permutations([i for i in range(9, 9 - len(char_list), -1)], len(char_list))
# )

# # print(char_list)
# # print(permutation_cases)
# for case in permutation_cases:
#     temp_result = 0
#     for string in alpha_list:
#         temp = ""
#         for c in string:
#             # print(c)
#             temp += str(case[char_list.index(c)])

#         temp_result += int(temp)
#     result = max(result, temp_result)

# print(result)

