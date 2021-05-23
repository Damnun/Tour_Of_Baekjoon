a, b = map(int, input().split())

if a > b:
    a, b = b, a

count = b - a - 1

if count <= 0:
    print(0)
    exit()

print(count)
for i in range(a+1, b):
    print(i, end=' ')
    
print()