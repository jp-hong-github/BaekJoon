import sys

input = sys.stdin.readline

student = [i for i in range(1, 31)]
for _ in range(28):
    temp = int(input())
    student.remove(temp)

student.sort()
print(student[0])
print(student[1])
