n = int(input())
num = n % 5
count = 0

if n == 1 or n == 3:
    print(-1)

elif num % 2 == 0:
    print(n // 5 + num // 2)

else:
    print((n // 5) - 1 + (num + 5) // 2)
