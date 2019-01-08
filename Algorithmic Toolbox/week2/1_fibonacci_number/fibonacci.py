# Uses python3
n = int(input())


def calc_fib(num):
    # Fibonacci using recursion
    if num <= 1:
        return num

    return calc_fib(num - 1) + calc_fib(num - 2)


print(calc_fib(n))
