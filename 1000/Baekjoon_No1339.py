n = int(input())
result = 0
num = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
dict_data = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0
             , 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0
             , 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, '!': 0}
data = []
for _ in range(n):
    data.append(input())
data = sorted(data, key=lambda x: len(x), reverse=True)
max_len = len(data[0])

for i in range(len(data)):
    if len(data[i]) != max_len:
        tmp = max_len - len(data[i])
        for _ in range(tmp):
            data[i] = '!' + data[i]

for i in range(len(data)):
    for j in range(max_len):
        dict_data[data[i][j]] += (10 ** (max_len - j - 1))

dict_data['!'] = 0
weights = []
for i in dict_data.values():
    if i != 0:
        weights.append(i)
weights.sort(reverse= True)

for i in weights:
    result += i * num.pop(0)
print(result)
