from math import factorial as f
n, c = map(int, input().split())

if 0 > c or c > n:
    print('0')

else:
    print(f(n)//(f(c)*f((n-c))))
