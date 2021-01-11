import sys

for index in range(int(sys.stdin.readline().rstrip())):
    b ,c = map(int,sys.stdin.readline().split())
    print(int(b)+int(c))
