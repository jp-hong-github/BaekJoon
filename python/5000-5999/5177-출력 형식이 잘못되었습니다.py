import sys
import re

input = sys.stdin.readline


def convert_str(s: str):
    s = s.lower()

    temp_s = s
    while True:
        for i in [" [", " (", " {", "[ ", "( ", "{ ", "[", "{"]:
            s = s.replace(i, "(")
        for i in [" ]", " )", " }", "] ", ") ", "} ", "]", "}"]:
            s = s.replace(i, ")")
        if temp_s == s:
            break
        else:
            temp_s = s

    temp_s = s
    while True:
        for i in [" ,", ", ", ",", " ;", "; "]:
            s = s.replace(i, ";")
        if temp_s == s:
            break
        else:
            temp_s = s

    temp_s = s
    while True:
        for i in [" :", ": "]:
            s = s.replace(i, ":")
        if temp_s == s:
            break
        else:
            temp_s = s

    temp_s = s
    while True:
        s = re.sub(r"\s+", " ", s)
        if temp_s == s:
            break
        else:
            temp_s = s

    return s


def compare_strings(s1: str, s2: str, idx):
    s1 = convert_str(s1)
    s2 = convert_str(s2)
    if s1 == s2:
        print(f"Data Set {idx}: equal")
    else:
        print(f"Data Set {idx}: not equal")


K = int(input())
for i in range(K):
    # 문자열의 맨 앞 혹은 맨 뒤 공백 제거
    s1 = input().strip()
    s2 = input().strip()
    compare_strings(s1, s2, i + 1)
    if i != K - 1:
        print()
