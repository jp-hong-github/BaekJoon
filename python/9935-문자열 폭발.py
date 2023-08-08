import sys

input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

stack = []
last_bomb = bomb[-1]
bomb_length = len(bomb)

# print(string[-1-bomb_length:]==bomb[:])

for char in string:
    stack.append(char)
    # print(char == last_bomb,stack[-bomb_length:] == bomb[:],stack[-bomb_length:])
    if char == last_bomb and "".join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]

answer = "".join(stack)

if len(stack) == 0:
    print("FRULA")
else:
    print(answer)
