data_number = int(input())
data = input()
after_data = []
index = 0

    
while index < data_number :
    if data[index] == 'L':
        after_data.append('C')
        index += 2
    else:
        after_data.append('S')
        index += 1

result = ['*']
for i in after_data:
    result.append(i)
    result.append('*')

if data_number >= result.count('*'):
    print(result.count('*'))
else:
    print(data_number)
