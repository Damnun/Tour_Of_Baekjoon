a, b = map(int, input().split())
gcd = a
tmp = b
while b != 0:
    r = gcd % b
    gcd = b
    b = r

print(gcd)
print(a*tmp//gcd)
