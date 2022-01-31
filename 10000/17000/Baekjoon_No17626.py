n = int(input())
d = [0, 1]

for i in range(2, n + 1):
    ans = float('inf')
    j = 1

    while (j ** 2) <= i:
        ans = min(ans, d[i - (j ** 2)])
        j += 1
    d.append(ans + 1)
print(d[n])
