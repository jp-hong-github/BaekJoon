import sys

input = sys.stdin.readline


primes_check = [False, False] + [True] * 999999
primes = []
for i in range(1000000):
    if primes_check[i] == True:
        primes.append(i)
        for k in range(2 * i, 1000000, i):
            primes_check[k] = False

while True:
    num = int(input())
    if num == 0:
        break

    temp = False
    for i in primes:
        if primes_check[num - i]:
            print(f"{num} = {i} + {num-i}")
            temp = True
            break

    if temp is False:
        print("Goldbach's conjecture is wrong.")
