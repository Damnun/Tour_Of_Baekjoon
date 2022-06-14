n = int(input())
a = 0

for _ in range(n):
    if int(input()) == 1:
        a += 1

if a > n // 2:
    print("Junhee is cute!")
    
else:
    print("Junhee is not cute!")
