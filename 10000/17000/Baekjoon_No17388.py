a, b, c = map(int, input().split())
if a+b+c >= 100:
    print("OK")
else:
    tmp = min(a, b, c)
    if tmp == a:
        print("Soongsil")
    elif tmp == b:
        print("Korea")
    else:
        print("Hanyang")
