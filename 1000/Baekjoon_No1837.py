P, K = map(int, input().split())
li = [1] * K

for i in range(2, int(K ** 0.5) + 1):
    if li[i] == 1:
        for j in range(i + i, K, i):
            li[j] = 0
p = [i for i in range(2, K) if li[i] == 1]

g, b = 1, 0
for n in p:
    if P % n == 0:
        g, b = 0, n
        break
        
print("GOOD" if g else f"BAD {b}")
