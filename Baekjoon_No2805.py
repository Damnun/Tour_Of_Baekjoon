import sys
input = sys.stdin.readline
tree_count, wood = map(int, input().split())
tree = list(map(int, input().split()))
start, end = min(tree), max(tree)
while start <= end:
    mid = (start + end) // 2
    data = 0
    for i in tree:
        data += i - mid if i - mid > 0 else 0
    if data >= wood: start = mid + 1
    else: end = mid - 1
print(end)


"""
4 7
20 15 10 17
def binarySearch(target):
    start,end=0, max(tree)
    ans = 0
    while(start<=end):
        mid = (start+end)//2
        Sum = treeSum(mid)
        if Sum < target :
            end = mid -1
        if Sum >= target:
            ans = mid
            start = mid + 1

    return ans
"""