import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
list_permutation_numbers = list(permutations(numbers, N))

result = 0

for case in list_permutation_numbers:
    result_case = 0
    circle_slice_idx_0_to_9 = [False] * 100
    circle_slice_idx_0_to_9[0] = True
    """
    이등분하는 선이 만들어지는 경우의 수
    00 ~ 50
    10 ~ 60
    20 ~ 70
    30 ~ 80
    40 ~ 90

    1 ~ 51
    ... 차이가 50이 되면 됨
    """

    current_pointing = 0
    for number in case:
        current_pointing += number
        if current_pointing >= 100:
            continue
        circle_slice_idx_0_to_9[current_pointing] = True

    for i in range(0, 50):
        if (
            circle_slice_idx_0_to_9[i] is True
            and circle_slice_idx_0_to_9[i + 50] is True
        ):
            result_case += 1
    result = max(result, result_case)

print(result)
