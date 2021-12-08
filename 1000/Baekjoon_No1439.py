s = input()
s2 = ''

for i in s:
    if i == '0':
      s2 += '1'
    else:
        s2 += '0'

a = s.split('1')
b = s2.split('1')
result = min((len(a) - a.count('')), (len(b) - b.count('')))
print(result)

