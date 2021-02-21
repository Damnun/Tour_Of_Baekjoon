import sys
data_count = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

search_count = int(sys.stdin.readline())
search = list(map(int, sys.stdin.readline().split()))

data.sort()
count = 0
for i in search:
    left = 0
    right = data_count -1
    while left <= right:
        mid = (left+right)//2
        if data[mid] == i:
            count = -1
            break
        elif data[mid]>i:
            right = mid-1
        elif data[mid]<i:
            left = mid+1
        count += 1

    if count == -1:
        print("1")
    else:
        print("0")
    count = 0