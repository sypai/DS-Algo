## Fibonacci Number

Recall the definition of Fibonacci sequence: F0 = 0, F1 = 1, and Fi = Fi−1 + Fi−2 for
i ≥ 2.

    Fibonacci(n):
    if n ≤ 1:
        return n
    return Fibonacci(n − 1) + Fibonacci(n − 2)
