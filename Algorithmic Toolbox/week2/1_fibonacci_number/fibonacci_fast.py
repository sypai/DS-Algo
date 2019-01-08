# Uses python3
fib_series = [0, 1]


def fib_calc(num):

    for i in range(2, num+1):
        curr = fib_series[i-1] + fib_series[i-2]
        fib_series.append(curr)

    return fib_series[num]


n = int(input())
print(fib_calc(n))

