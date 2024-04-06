import sys

input = sys.stdin.readline


def cal(args):
    return 6 * args[0] + 3 * args[1] + 2 * args[2] + 1 * args[3] + 2 * args[4]


A = list(map(int, input().split()))
B = list(map(int, input().split()))

print("%d %d" % (cal(A), cal(B)))
