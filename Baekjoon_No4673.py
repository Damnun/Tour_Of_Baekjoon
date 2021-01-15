dn = []

for i in range(10000):
    if i == 0:
        continue

    elif i > 0 and i < 10:
        result = i*2
        dn.append(result)

    elif i >= 10 and i < 100:
        result = (i + int(i / 10) + int(i % 10))
        dn.append(result)

    elif i >= 100 and i < 1000:
        result = (i + int(i / 100) + int(i % 100 / 10) + int(i % 100 % 10))
        dn.append(result)

    elif i >= 1000 and i < 10000:
        result = (i + int(i / 1000) + int(i % 1000 / 100) +
                  int(i % 1000 % 100 / 10) + int(i % 1000 % 100 % 10))
        dn.append(result)


for i in range(10000):
    if i == 0:
        continue
    elif dn.count(i) == 0:
        print(i)
