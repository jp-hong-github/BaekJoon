import sys

input = sys.stdin.readline

result_lst = []
T = int(input())
for _ in range(T):
    password = input().rstrip()
    front_string = []
    rear_string = []
    for c in password:
        if c == "<":
            if len(front_string) != 0:
                rear_string.append(front_string.pop())
        elif c == ">":
            if len(rear_string) != 0:
                front_string.append(rear_string.pop())
        elif c == "-":
            if len(front_string) != 0:
                front_string.pop()
        else:
            front_string.append(c)

    rear_string.reverse()
    result_lst.append(front_string + rear_string)


for result in result_lst:
    print("".join(str(s) for s in result))
