import sys
input = sys.stdin.readline

n = int(input())
a = []
b = 0

if n > 1:
    a = [n]

while True:
    if a == []:
        print(b)
        break
    else:
        x = a.pop()
        a1 = x // 2
        a2 = x - a1
        b += a1 * a2
        
        if a1 != 1:
            a.append(a1)
        
        if a2 != 1:
            a.append(a2)
