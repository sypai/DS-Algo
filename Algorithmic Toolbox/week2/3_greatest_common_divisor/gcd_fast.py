# Uses python3
# Euclidan Algorithm

# Uses python3
a, b = [int(x) for x in input().split()]


def find_gcd(num, den):
    if den == 0:
        return num

    num_rem = num % den
    return find_gcd(den, num_rem)


print(find_gcd(a, b))

