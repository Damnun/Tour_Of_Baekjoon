import sys
loop = int(sys.stdin.readline().rstrip())
check_list = [0] * 10001
for _ in range(loop):
    data = (int(sys.stdin.readline().rstrip()))
    check_list[data] += 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)
