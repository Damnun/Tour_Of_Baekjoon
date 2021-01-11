while True:
    h, m = input().split()
    h = int(h)
    m = int(m)

    if h >= 0 and h <= 23:
        break
    if m >= 0 and h <= 59:
        break

if m >= 45:
    m -= 45

else:
    if h-1 < 0:
        h = 23
    else:
        h -= 1
    m += 15

print(h, m)