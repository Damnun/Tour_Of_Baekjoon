a = ['0', '0', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

b = input()
result = 0

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] in a[j]:
            result += (j+1)

print(result)
