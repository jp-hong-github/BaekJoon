import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))

result = 1

n_mod_k = n % k

remainder_set = set()

current_remainder = n_mod_k
ten_mod_k = 10 ** len(str(n)) % k

remainder_to_add = 1

while True:
    if current_remainder == 0:
        break
    else:
        if current_remainder in remainder_set:
            result = -1
            break

        remainder_set.add(current_remainder)

        remainder_to_add = remainder_to_add * ten_mod_k % k
        current_remainder += n_mod_k * remainder_to_add % k
        current_remainder = current_remainder % k
        result += 1


print(result)
