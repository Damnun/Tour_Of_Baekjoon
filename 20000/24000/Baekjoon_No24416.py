def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    count = 0
    a[1] = a[2] = 1
    for i in range(3, n + 1):
        count += 1
        a[i] = a[i - 1] + a[i - 2]
    return count

n = int(input())
a = [0] * (n + 1)
print(fib(n), fibonacci(n))
