# Uses python3


def get_primes(num):
    primes = []
    if num == 2:
        return primes.append(2)

    if num == 3:
        return primes.append([2, 3])

    if num > 3:
        primes.append(2)
        primes.append(3)

    for i in range(4, num):
        for j in range(2, i):
            if i % j == 0:
                break

            if j == len(range(2, i))-1:
                primes.append(i)

    return primes
