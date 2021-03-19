import sys

data = set()
loop = int(input())

for i in range(loop):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            data = set([i for i in range(1, 21)])
        else:
            data = set()
        continue

    command, target = tmp[0], int(tmp[1])

    if command == 'add':
        data.add(target)
    elif command == 'check':
        print(1 if target in data else 0)
    elif command == 'remove':
        data.discard(target)
    elif command == 'toggle':
        if target in data:
            data.discard(target)
        else:
            data.add(target)