n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0

tmp = 0
for i in data:
    tmp += i
    result += tmp
print(result)