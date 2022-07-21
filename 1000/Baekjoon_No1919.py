a = [0] * 26

for i in list(input()):
    a[ord(i) - 97] += 1
for j in list(input()):
    a[ord(j) - 97] -= 1
print(sum(map(abs, a)))
