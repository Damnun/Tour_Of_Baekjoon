while True:
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a >= 1 and c <= 10000 : break


print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
