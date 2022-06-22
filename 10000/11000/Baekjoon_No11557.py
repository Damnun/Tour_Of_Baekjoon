for _ in range(int(input())):
    a = []
    for _ in range(int(input())):
        s, l = map(str, input().split())
        a.append([s, int(l)])
    a = sorted(a, key = lambda x: x[1])
    print(a[-1][0])
