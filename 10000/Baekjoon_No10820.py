import sys
input = sys.stdin.readline

while True:
    data = input().rstrip('\n')

    if not data:
        break

    l, u, d, s = 0, 0, 0, 0
    for now in data:
        if now.islower():
            l += 1
        elif now.isupper():
            u += 1
        elif now.isdigit():
            d += 1
        elif now.isspace():
            s += 1
    print(l, u, d, s)
