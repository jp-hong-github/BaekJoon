import sys

input = sys.stdin.readline

prime = [True] * 10001
prime[0] = False
prime[0] = False

prime_number = []
for i in range(2, 10001):
    if prime[i] == True:
        prime_number.append(i)
        for k in range(2 * i, 10001, i):
            prime[k] = False

gold_list = [[0, 1000000] for _ in range(10001)]  # 대강 차이가 많이 나도록 숫자를 선택함.숫자의 의미는 없음
for i in range(len(prime_number) - 1):
    for k in range(i, len(prime_number)):
        idx = prime_number[i] + prime_number[k]
        if idx < len(gold_list) and (gold_list[idx][1] - gold_list[idx][0]) > (prime_number[k] - prime_number[i]):
            gold_list[idx][1] = prime_number[k]
            gold_list[idx][0] = prime_number[i]

t = int(input())
for _ in range(t):
    number = int(input())
    print(*gold_list[number])

