MAX = 46
a, b = map(int, input().split())
 
arr = [0]
for i in range(MAX):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))
