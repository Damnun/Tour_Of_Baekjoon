start, end = map(int, input().split())
validation = [False for _ in range(end - start + 2)]
count = end - start + 1
i = 2

while i**2 <= end:
    tmp = start // (i**2)
    if start % (i**2) != 0:
        tmp += 1

    while tmp * (i**2) <= end:
        if not validation[tmp * (i**2) - start]:
            validation[tmp * (i**2) - start] = True
            count -= 1
        tmp += 1
    i += 1
print(count)

"""
에라토스테네스의 체를 이용하여 소수와 소수의 제곱으로 나누어지는 수를 걸러주면 되는 문제였는데
최댓값이 10000000000000 수준이라 시간초과를 해결 하는게 관건인 문제였다.
end - start를 나눌 수 있는 최소값을 정해 그 값에서부터 1씩 올라가며 (end보단 작게) 소수 나눔을 해주는
소거법으로 풀어보았다. 어렵군 어려워
"""