str1 = input()
str2 = input()
data_one = []
data_two = []
dp = []
result = 0

for i in range(len(str1)):
    data_one.append(str1[i])

for i in range(len(str2)):
    data_two.append(str2[i])

data = set(data_one) & set(data_two)
del(data_one)
del(data_two)

data = sorted(list(data))
dp.append(data[0])

print(data)

