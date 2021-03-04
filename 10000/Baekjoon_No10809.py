s = input()

i = 97
while i != 123:
    if chr(i) in s:
        print(s.index(chr(i)), end=' ')
    else:
        print("-1", end=' ')
    i += 1
