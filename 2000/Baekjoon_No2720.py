for _ in range(int(input())):
    c = int(input())
    d = [25, 10, 5, 1]
    a = []
    for n in d:
        a.append(c // n)
        c %= n
    print(*a)
