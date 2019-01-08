# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


if __name__ == '__main__':
    in_put = sys.stdin.read()
    a, b = map(int, in_put.split())
    print(lcm_naive(a, b))
