import math, sys
input = sys.stdin.readline
array = [True for i in range(10001)]

for i in range(2, 101):
    if array[i]:
        j = 2
        while i * j <= 10000:
            array[i * j] = False
            j += 1

for _ in range(int(input())):
    target = int(input())
    x = target // 2
    y = x

    for _ in range(10000):
        if array[x] and array[y]:
            print(x, y)
            break
        x -= 1
        y += 1
