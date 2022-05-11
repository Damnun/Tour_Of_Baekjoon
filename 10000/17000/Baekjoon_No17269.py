# 획 순을 미리 지정
alphabet = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

n, m = map(int, input().split())
a, b = input().split()
ab = ""
end = min(n, m)

for i in range(end):
    ab += a[i] + b[i]
ab += a[end:] + b[end:]

data = [alphabet[ord(i) - ord('A')] for i in ab]

for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        data[j] += data[j + 1]

print("{}%".format(data[0] % 10 * 10 + data[1] % 10))
