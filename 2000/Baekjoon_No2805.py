import sys
input = sys.stdin.readline
tree_count, wood = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, 1000000000

while start <= end:
    mid = (start + end) // 2

    data = 0
    for i in tree:
        if i - mid > 0:
            data += i - mid

    if data >= wood:
        start = mid + 1
    else:
        end = mid - 1
print(end)