from Tests.Program import assert_equal


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return not is_even(num)


def power(x, n):
    print("Computing ", x, " raised to the power ", n, ".")
    # Base Case
    if n == 0:
        return 1

    # n is negative
    if n < 0:
        return 1/power(x, -n)

    # n is positive and odd
    if is_odd(n):
        return power(x, n-1)*x

    # If n is positive and even
    if is_even(n):
        y = power(x, n/2)
        return y*y


def display_power(x, n):
    print(x, " to the ", n, " is ", power(x, n))


display_power(3, 0)
assert_equal(power(3, 0), 1)
print("\n")
display_power(2, 5)
assert_equal(power(2, 5), 32)
print("\n")
display_power(4, 4)
assert_equal(power(4, 4), 256)
print("\n")
display_power(5, -2)
assert_equal(power(5, -2), 1/25)



