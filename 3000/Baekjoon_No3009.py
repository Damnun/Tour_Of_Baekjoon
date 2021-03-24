dp_x = []
dp_y = []
for _ in range(3):
    x, y = map(int, input().split())
    dp_x.append(x)
    dp_y.append(y)

for i in range(3):
    if dp_x.count(dp_x[i]) == 1:
        a = dp_x[i]
    if dp_y.count(dp_y[i]) == 1:
        b = dp_y[i]
print(a, b)
