a = input()
b = input()
a = int(a)

for num in range(len(b)):
    index = len(b) - num - 1
    result = a * int(b[index])
    print(result)
    num -= 1

result = a * int(b)
print(result)
