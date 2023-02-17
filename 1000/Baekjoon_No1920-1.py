n = int(input())
data = list(map(int, input().split()))
data.sort()

s = int(input())
search = list(map(int, input().split()))


def binary(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary(array, target, start, mid - 1)
    else:
        return binary(array, target, mid + 1, end)


for i in search:
    result = binary(data, i, 0, n - 1)
    result = 1 if result else 0
    print(result)
