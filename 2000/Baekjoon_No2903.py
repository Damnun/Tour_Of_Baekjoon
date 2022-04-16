n = int(input())
a, f, b, sum = [4], 2, 1, 0

for i in range(1, 16):
    f += b
    sum = f ** 2
    a.append(sum)
    b *= 2
    
print(a[n])
