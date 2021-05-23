word_count = int(input())
data = input()
result = 0

for i in range(word_count):
    result += (ord(data[i]) - 96) * (31**i)
print(result % 1234567891)