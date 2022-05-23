a = []
c = []
ans = 0
tmp = []

for i in range(8):
    a.append(int(input()))
    
b = sorted(a, reverse=True)

for i in range(5):
    c.append(b[i])
    
for i in c:
    ans += i
    tmp.append(a.index(i))
print(ans)

s = sorted(tmp)
for i in s:
    print(i + 1, end=' ')
