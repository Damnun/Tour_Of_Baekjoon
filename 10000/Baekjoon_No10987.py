cur = input()
a = 'aeiou'
ans = 0

for i in a:
    ans += cur.count(i)
print(ans)
