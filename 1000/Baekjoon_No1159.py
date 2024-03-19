from collections import Counter
data = []
for _ in range(int(input())):
    data.append(input()[0])

result = []
data_Counter = Counter(data)

for i in data_Counter.keys():
    if data_Counter[i] >= 5:
        result.append(i)

if result:
    print("".join(sorted(result)))
else:
    print("PREDAJA")

