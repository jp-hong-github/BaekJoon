import sys

input = sys.stdin.readline

str_stack_1 = list(input().rstrip())
str_stack_2 = []
M = int(input())


for _ in range(M):
    order = list(map(str, input().split()))
    if len(order) == 1:
        if order[0] == "D" and str_stack_2:
            str_stack_1.append(str_stack_2.pop())

        elif order[0] == "L" and str_stack_1:
            str_stack_2.append(str_stack_1.pop())

        elif order[0] == "B" and str_stack_1:
            str_stack_1.pop()

    else:
        str_stack_1.append(order[1])


for ch in str_stack_1:
    print(ch, end="")

str_stack_2.reverse()
for ch in str_stack_2:
    print(ch, end="")
