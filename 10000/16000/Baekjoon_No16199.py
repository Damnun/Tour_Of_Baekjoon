y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
m = 0

if m1 < m2:
    m = y2 - y1
    
elif m1 == m2:
    if d1 <= d2:
        m = y2 - y1
    else:
        m = y2 - y1 -1
else:
    m = y2 - y1 -1

count = y2 - y1 +1
year = y2 - y1

print(m)
print(count)
print(year)
