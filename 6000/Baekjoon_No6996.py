import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(str, input().split())

    if sorted(list(a)) == sorted(list(b)):
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))
