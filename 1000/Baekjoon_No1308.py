from datetime import *
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y1 + 1000 < y2:
    print("gg")
elif y1 + 1000 == y2 and (m1, d1) <= (m2, d2):
    print("gg")
else:
    today = date(y1, m1, d1)
    d_day = date(y2, m2, d2)
    print(f"D-{str(d_day.toordinal() - today.toordinal())}")
    print(today)
    print(d_day)
    print(today.toordinal())
