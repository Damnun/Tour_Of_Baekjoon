import math
n = int(input())
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1


data = []
for i in range(2, n + 1):
    if array[i]:
        data.append(i)

while True:
    if n in data:
        print(n)
        break

    elif n == 1:
        break

    for i in range(2, n + 1):
        if n % i == 0:
            n //= i
            print(int(i))
            break
