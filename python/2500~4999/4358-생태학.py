import sys
from collections import defaultdict

# import decimal

# context = decimal.getcontext()
# context.rounding = decimal.ROUND_HALF_UP

input = sys.stdin.readline

trees = defaultdict(int)
total = 0

while True:
    line = sys.stdin.readline().rstrip("\n")

    if not line:
        break

    trees[line] += 1
    total += 1

for tree, count in dict(sorted(trees.items())).items():
    # print(tree, round(count / total * 100, 4))
    print("%s %.4f" % (tree, count / total * 100))
