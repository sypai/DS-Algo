# Calculating Factorial using Iteration

from Tests.Program import assert_equal  # A Test Function


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i

    return fact


print("The value of 4! is ", factorial(4))
assert_equal(factorial(4), 24)
print("The value of 5! is ", factorial(5))
assert_equal(factorial(5), 120)

