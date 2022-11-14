import sys

input = sys.stdin.readline

string = list(map(str, input().rstrip()))
string.sort()

len_string = len(string)
visited = [False for _ in range(len_string)]

result = set()


def check(char, count, str_list):
    global len_string, string, result
    if len_string == count:
        result.add(str(str_list))
        # print(*str_list)
    else:
        for next in range(0, len_string):
            if count == 0 or (
                visited[next] == False and abs(ord(char) - ord(string[next])) != 0
            ):
                visited[next] = True
                str_list.append(string[next])
                check(string[next], count + 1, str_list)
                str_list.pop()
                visited[next] = False


check(0, 0, [])
print(len(result))
