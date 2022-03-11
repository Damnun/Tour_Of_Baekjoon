"""
subsequence : 수열의 순서를 유지하며 만든 부분수열
substirng : 문자열의 연속된 일부분
LCS : Longest Common Subsequence

"""
a, b = input(), input()
n, m = len(a), len(b)
a = " " + a
b = " " + b
d = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i] == b[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])
print(d[n][m])
