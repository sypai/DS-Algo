# Uses python3
a, b = [int(x) for x in input().split()]


def find_gcd(num, den):
    gcd = 1
    ul = 0

    if num > den:
        ul = den
    else:
        ul = num

    for i in range(1, ul+1):
        if num % i == 0 and den % i == 0:
            gcd = i

    return gcd


print(find_gcd(a, b))
