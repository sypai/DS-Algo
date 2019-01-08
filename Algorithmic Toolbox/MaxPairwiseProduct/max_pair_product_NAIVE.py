# python3

# n = int(input())
# a = [int(x) for x in input().split()]
# product = 0


def max_naive(a, n):
    product = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, a[i] * a[j])

    return product