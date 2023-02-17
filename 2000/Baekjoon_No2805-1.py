n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))


def binary(arr, start, end):
    if start > end:
        return end

    mid = (start + end) // 2
    count = 0
    for i in arr:
        if mid < i:
            count += (i - mid)

    if count == m:
        return mid
    elif count < m:
        return binary(arr, start, mid - 1)
    else:
        return binary(arr, mid + 1, end)

print(binary(data, 0, max(data)))
