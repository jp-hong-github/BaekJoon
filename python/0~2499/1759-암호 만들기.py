import sys

input = sys.stdin.readline

L, C = map(int, input().split())

string = list(map(str, input().split()))
string.sort()

vowel = ["a", "e", "i", "o", "u"]

visited = [False for _ in range(C)]


def check(char, idx, count, str_list, vowel_count):
    global C, string
    if L == count:
        if vowel_count >= 1 and L - vowel_count >= 2:
            for ch in str_list:
                print(ch, end="")
            print()
    else:
        for next in range(idx + 1, C):
            if count == 0 or (
                visited[next] == False and ord(string[next]) - ord(char) > 0
            ):
                visited[next] = True
                str_list.append(string[next])
                if string[next] in vowel:
                    check(string[next], next, count + 1, str_list, vowel_count + 1)
                else:
                    check(string[next], next, count + 1, str_list, vowel_count)

                str_list.pop()
                visited[next] = False


check(0, -1, 0, [], 0)
