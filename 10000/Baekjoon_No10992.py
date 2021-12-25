n = int(input())
for i in range(1, n):
    tmp = i * 2 - 1
    for _ in range(1, n - i + 1):
        print(" ", end='')
    print("*", end='')
    for _ in range((i - 1) * 2 - 1):
        print(" ", end='')
    if i != 1:
        print("*")
    else:
        print("")
print("*" * ((n * 2) - 1))
