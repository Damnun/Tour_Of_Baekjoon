import sys
input = sys.stdin.readline

data = input().rstrip()
ans = ''

for x in data:
    if 'a' <= x and x <= 'z':
        x = ord(x) + 13
        if x > 122:
            x -= 26
        ans += chr(x)
    elif 'A' <= x and x <= 'Z':
        x = ord(x) + 13
        if x > 90:
            x -= 26
        ans += chr(x)
    else:
        ans += x

print(ans)
