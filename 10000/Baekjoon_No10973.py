import sys
input = sys.stdin.readline

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] >= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
"""
i - 1번째가 a[i]보다 큰 가장 큰 i를 찾는다
2. 바꿔야 할 수 j를 찾는다 ( list[i:] 중에 제일 큰 수 )
3. i-1과 j를 바꾼다
4. 뒷 수열을 뒤집어준다
-> 오름차순
"""
