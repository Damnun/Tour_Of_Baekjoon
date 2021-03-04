import sys
data = int(input())
result = []
for _ in range(data):
    result.append(int(sys.stdin.readline()))

for i in sorted(result):
    sys.stdout.write(str(i)+'\n')
