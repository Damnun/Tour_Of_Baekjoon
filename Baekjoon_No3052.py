a = []; cnt = 0

for i in range(10):
    a.append(int(input()) % 42)

a = set(a)

print(len(a))
