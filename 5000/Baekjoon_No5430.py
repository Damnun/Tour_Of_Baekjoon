import sys
input = sys.stdin.readline
for _ in range(int(input())):
    commands = input()
    n = int(input())
    data = input().rstrip()[1:-1].split(",")
    result = 0
    reverse_count = 0

    if n == 0:
        data = []

    for command in commands:
        if command == 'R':
            reverse_count += 1

        elif command == 'D':
            if len(data) > 0:
                if reverse_count % 2 == 0:
                    data.pop(0)
                else:
                    data.pop()
            else:
                result = -1

    if reverse_count % 2 == 1:
        data.reverse()
    if result == -1:
        print("error")
    else:
        print("[" + ",".join(data) +"]")
