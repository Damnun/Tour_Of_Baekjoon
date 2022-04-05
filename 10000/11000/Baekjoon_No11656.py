a = str(input())
b = []
for _ in a:
    b.append(a)
    a = a[1:]
for i in sorted(b):
    print(i)
    
