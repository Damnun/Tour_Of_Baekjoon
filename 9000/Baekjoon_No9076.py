for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.remove(max(a))
    a.remove(min(a))
    if max(a) - min(a) >= 4:
        print('KIN')
    else:
        print(sum(a))
