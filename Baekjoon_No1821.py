n, k = map(int, input().split())
a = []
a.append(n-(k-1))
for i in range(k-1):
    a.append(1)
print(a)

index = 0
while True:
    if a[0] < a[1]:
        break
    elif a[index] > a[index+1] and a[index+1]+1 > a[index+2]:
        a[index] -= 1
        a[index+1] += 1
    print(a, index)
    index += 1