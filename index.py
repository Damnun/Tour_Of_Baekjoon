a = int(input())
for i in range(a):
    b, c = input().split()
    result = int(b) + int(c)
    print("Case #%d: %d" %(i+1, result))
