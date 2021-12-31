n = int(input())
count = 0
start, length = 1, 1
while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    count += (end - start + 1) * length
    start *= 10
    length += 1
print(count)
