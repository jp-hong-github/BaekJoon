import sys

input = sys.stdin.readline

N = int(input())
result = []


def check_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def backtracking(number):
    global N
    if len(str(number)) == N:
        result.append(number)
        return
    else:
        for i in [1, 3, 7, 9]:
            if check_prime(number * 10 + i):
                backtracking(number * 10 + i)


for i in [2, 3, 5, 7]:
    backtracking(i)

for num in result:
    print(num)
