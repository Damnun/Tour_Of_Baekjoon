data = input()
tmp = 0
for i in range(len(data) // 10):
    print(data[tmp:(tmp + 10)])
    tmp += 10
if len(data) % 10 != 0:
    print(data[tmp:(tmp + (len(data) % 10))])
