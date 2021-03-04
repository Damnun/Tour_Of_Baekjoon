a, b = map(int, input().split())
c = input().split(" ")
result = a*b
for i in range(len(c)):
    c[i] = int(c[i]) - result
    print(c[i], end=' ')
