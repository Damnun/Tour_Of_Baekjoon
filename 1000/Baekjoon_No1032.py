n = int(input())
a = list(input())

l = len(a)
for i in range(n - 1):
    b = list(input())
    
    for j in range(l):
        if a[j] != b[j]:
            a[j] = '?'

print(''.join(a))
