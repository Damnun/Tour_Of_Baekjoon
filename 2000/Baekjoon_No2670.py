n = int(input())
data = [float(input()) for _ in range(n)]
for i in range(1, n):
    data[i] = max(data[i], data[i] * data[i - 1])
print("%.3f" % (max(data)))

"""
8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4"""
