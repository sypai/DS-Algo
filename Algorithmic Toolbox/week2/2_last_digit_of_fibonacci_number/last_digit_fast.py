# Uses python3
n = int(input())
fib_series = [0,1]


def last_of_fib(num):

    for i in range(2, num+1):
        curr = (fib_series[i-1] + fib_series[i-2]) % 10
        fib_series.append(curr)

    return fib_series[num]


print(last_of_fib(n))
