import sys
from collections import deque
result = deque()
input_count = int(sys.stdin.readline())
for _ in range(input_count):
    data = list(sys.stdin.readline().split())
    if data[0] == 'push':
        result.append(int(data[1]))
        
    elif data[0] == 'top':
        if len(result) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(result[len(result)-1]))
            sys.stdout.write("\n")
        
    elif data[0] == 'size':
        sys.stdout.write(str(len(result)))
        sys.stdout.write("\n")
        
    elif data[0] == 'pop':    # pop이 불가할 경우 -1로 예외처리
        if len(result) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(result.pop()))
            sys.stdout.write("\n")
            
    elif data[0] == 'empty':
        if len(result) == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
