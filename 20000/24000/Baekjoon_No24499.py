n, k = map(int, input().split())
a = list(map(int, input().split()))
result = 0
sum = 0

for i in range(k - 1):
    a.append(a[i])


for i in range(k):
    sum += a[i]

result = sum

for i in range(k, len(a)):
    sum += a[i] - a[i - k]
    result = max(result, sum)

# print(a)
print(result)
