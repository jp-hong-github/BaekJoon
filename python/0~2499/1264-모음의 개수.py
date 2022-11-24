import sys

input = sys.stdin.readline
result_list = []
while True:
    string = list(map(str, input().rstrip()))
    # print(string)
    if "#" in string:
        break
    else:
        result = 0
        for c in string:
            if c.lower() in ["a", "e", "i", "o", "u"]:
                result += 1

        result_list.append(result)

for r in result_list:
    print(r)
