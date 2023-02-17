k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
data.sort()

def binary(arr, start, end):
    if start > end:
        return end

    mid = (start + end) // 2
    lines = 0

    for i in data:
        lines += i // mid

    if lines >= n:
        return binary(arr, mid + 1, end)
    else:
        return binary(arr, start, mid - 1)


print(binary(data, 1, data[-1]))

