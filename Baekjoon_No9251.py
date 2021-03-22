str1 = input()
str2 = input()
data_one = []
data_two = []

for i in range(len(str1)):
    data_one.append(str1[i])

for i in range(len(str2)):
    data_two.append(str2[i])

data_one = set(data_one)
data_two = set(data_two)
print(len(data_one & data_two))

"""
ACAYKP
CAPCAK
"""