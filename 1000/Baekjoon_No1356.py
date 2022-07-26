n = input()
ans = 0
for i in range(len(n) - 1):
    l, r = 1, 1
    for j in range(i + 1):
        l *= int(n[j])
        
    for k in range(i + 1, len(n)):
        r *= int(n[k])
        
    if l == r:
        print("YES")
        ans = 1
        break
        
if ans == 0:
    print("NO")
