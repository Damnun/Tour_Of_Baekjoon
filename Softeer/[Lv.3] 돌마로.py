k, p, n = map(int, input().split())
n *= 10


def solution(x, y):
    if y == 1:
        return x

    elif y % 2 == 0:
        a = solution(x, y / 2)
        return a * a % 1_000_000_007

    else:
        b = solution(x, (y - 1) / 2)
        return b * b * x % 1_000_000_007
        

result = solution(p, n)
result *= k
print(result % 1_000_000_007)
