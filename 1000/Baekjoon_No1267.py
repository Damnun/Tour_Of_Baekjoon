n = int(input())
s = list(map(int, input().split()))
year = 0
month = 0

for i in s:
    year += i // 30 * 10 + 10
    month += i // 60 * 15 + 15
    
if year < month:
    print('Y %d' % year)
elif year > month:
    print('M %d' % month)
else:
    print('Y M %d' % year)
