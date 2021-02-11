result = [1, 1, 2, 2, 2, 8]
a = input().split(" ")
for i in range(len(result)):
    result[i] -= int(a[i])
    print(result[i], end=' ')
