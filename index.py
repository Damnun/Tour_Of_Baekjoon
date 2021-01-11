a = int(input())
for i in range(a):
    b, c = input().split()
    b = int(b)
    c = int(c)
    result = b + c
    print("Case #%d: %d + %d = %d" %(i+1, b, c, result))
