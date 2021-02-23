import sys
from collections import deque
result = deque()
input_count = int(sys.stdin.readline())
for _ in range(input_count):
    data = list(sys.stdin.readline().split())

    if data[0] == 'push_front':
        result.appendleft(data[1])
        
    elif data[0] == 'push_back':
        result.append(data[1])
        
    elif data[0] == 'size':
        sys.stdout.write(str(len(result)))
        sys.stdout.write("\n")
        
    elif data[0] == 'pop_front':    # pop이 불가할 경우 -1로 예외처리
        if len(result) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(result.popleft()))
            sys.stdout.write("\n")
            
    elif data[0] == 'pop_back':    # pop이 불가할 경우 -1로 예외처리
        if len(result) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(result.pop()))
            sys.stdout.write("\n")
            
    elif data[0] == 'back':
        if len(result) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(result[len(result)-1]))
            sys.stdout.write("\n")

    elif data[0] == 'front':
        if len(result) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(result[0]))
            sys.stdout.write("\n")

    elif data[0] == 'empty':
        if len(result) == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
            
            
