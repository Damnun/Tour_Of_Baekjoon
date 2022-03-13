n = int(input())
check = [False] * (n + 1) # 소수 판별
primes = [] # 소수
for i in range(2, n + 1):
    if check[i]:
        continue
    j = i * 2
    primes.append(i)
    while j <= n:
        check[j] = True
        j += i

ans, left, right = 0, 0, 0
sum = 0 if len(primes) == 0 else primes[0]

while left <= right < len(primes):
    if sum <= n:
        if sum == n:
            ans += 1
        right += 1
        if right < len(primes):
            sum += primes[right]
    else:
        sum -= primes[left]
        left += 1
print(ans)
