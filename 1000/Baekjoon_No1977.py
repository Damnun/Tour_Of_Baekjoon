m = int(input())
n = int(input())
a = []
i = 1

while i**2 <= n:
    if m <= i**2 <= n:
        a.append(i**2)
    i += 1
    
if not len(a):
    print(-1)
    
else:
    print(sum(a))
    print(a[0])
