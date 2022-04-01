data = []
ans = 0 

for _ in range(4) :
    o, i = map(int,input().split())
    ans += i 
    ans -= o 
    data.append(ans)
    
print(max(data))
