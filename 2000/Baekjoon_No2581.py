import math
start = int(input())
end = int(input())

if start == 1:
    start = 2

array = [True for i in range(end + 1)]

for i in range(2, int(math.sqrt(end)) + 1):
    if array[i]:
        j = 2
        while i * j <= end:
            array[i * j] = False
            j += 1

result = 0
data = []
for i in range(start, end + 1):
    if array[i]:
        data.append(i)
        result += i

if data:
    print(result)
    print(min(data))
else:
    print("-1")
