n = int(input())
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = d[i - 1] + 1  # a만 입력
    for j in range(1, i - 2):
        d[i] = max(d[i], d[i - j - 2] * (j + 1))
print(d[n])
