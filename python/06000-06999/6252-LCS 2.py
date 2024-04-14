import sys

input = sys.stdin.readline

s1 = list(map(str, input().rstrip()))
s1.insert(0, 0)
s2 = list(map(str, input().rstrip()))
s2.insert(0, 0)

matrix = [["" for _ in range(len(s1))] for __ in range(len(s2))]
result = []

for s1_idx in range(1, len(s1)):
    for s2_idx in range(1, len(s2)):
        if s1[s1_idx] == s2[s2_idx]:
            matrix[s2_idx][s1_idx] = matrix[s2_idx - 1][s1_idx - 1] + s1[s1_idx]
        else:
            if len(matrix[s2_idx - 1][s1_idx]) >= len(matrix[s2_idx][s1_idx - 1]):
                matrix[s2_idx][s1_idx] = matrix[s2_idx - 1][s1_idx]
            else:
                matrix[s2_idx][s1_idx] = matrix[s2_idx][s1_idx - 1]

print(len(matrix[-1][-1]))
print(matrix[-1][-1])
