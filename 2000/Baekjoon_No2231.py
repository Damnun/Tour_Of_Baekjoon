import math
data = input()

for i in range(1, int(data)+1): # 1 ~ 216까지
    tmp = str(i)
    summer = int(i)
    
    for j in range(int(math.log10(i))+1): # 1자리 1회 2자리 2회 3자리 3회... [0][1][2] .. [0][1] .. [0]..
        summer += int(tmp[j])
    
    if summer == int(data):
        result = i
        break
    else:
        result = 0

print(result)