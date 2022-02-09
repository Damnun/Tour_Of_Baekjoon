n = int(input())
a = list(map(int, input().split()))
a = sorted(list(set(a)))
print(*a)
