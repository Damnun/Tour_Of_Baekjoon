import sys
input = sys.stdin.readline

def power(x, n):
    if n == 1:
        return x
    elif n % 2:
        return multi(power(x, n - 1), x)
    else:
        return power(multi(x, x), n // 2)


def multi(a, b):
    tmp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            tmp[i][j] = sum % 1000000007
    return tmp


x = [[1, 1], [1, 0]]
start = [[1], [1]]
n = int(input())
if n < 3:
    print(1)
else:
    print(multi(power(x, n - 2), start)[0][0])
