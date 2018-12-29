# Calculating Factorial using Recursion

from Tests.Program import assert_equal  # A Test Function


def factorial(num):
    # Base case
    if num == 0:
        return 1

    # Recursive case
    return num * factorial(num-1)


print("The value of 4! is ", factorial(4))
assert_equal(factorial(4), 24)
print("The value of 5! is ", factorial(5))
assert_equal(factorial(5), 120)
print("The value of 10! is ", factorial(10))
assert_equal(factorial(10), 3628800)

