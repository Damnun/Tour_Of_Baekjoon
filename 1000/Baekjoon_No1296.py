x = input()
n = int(input())
a = sorted([input() for i in range(n)])
mp = mi = 0
for i in range(n):
    L = x.count("L") + a[i].count("L")
    O = x.count("O") + a[i].count("O")
    V = x.count("V") + a[i].count("V")
    E = x.count("E") + a[i].count("E")
    p = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    if mp < p:
        mp = p
        mi = i
print(a[mi])
