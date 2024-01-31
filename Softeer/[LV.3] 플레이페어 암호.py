message = input()
key = input()
maps = []
data = []

# 암호키 테이블 만들기 (가로축 데이터 맵)
for i in range(len(key)):
    if key[i] not in maps:
        maps.append(key[i])
            
for i in range(65, 92):
    if chr(i) not in maps and chr(i) != 'J':
        maps.append(chr(i))
maps = maps[:25]
tmp_maps = maps # 일차원 데이터 맵

for _ in range(5):
    data.append(maps[:5])
    maps = maps[5:]

# 세로축 데이터 맵
col_data = []
for i in range(5):
    tmp = ""
    for j in range(5):
        tmp += data[j][i]
    col_data.append(tmp)


# 메시지 나누기
token = 0
tmp_message = message


while True:
    flag = True
    for i in range(0, len(tmp_message), 2):
        m = tmp_message[i:i + 2]
        if len(m) == 2 and m[0] == m[1]:
            flag = False
            if m[0] != 'X':
                tmp_message = tmp_message[:i + 1] + 'X' + tmp_message[i + 1:]
            else:
                tmp_message = tmp_message[:i + 1] + 'Q' + tmp_message[i + 1:]
            break
    if flag:
        break
        
if len(tmp_message) % 2 != 0:
    tmp_message += 'X'
    
message = []
for i in range(len(tmp_message) // 2):
    message.append(tmp_message[:2])
    tmp_message = tmp_message[2:]


# 메시지 암호화
def row_check(token):
    for i in range(5):
        tmp = ""
        if token[0] in data[i] and token[1] in data[i]:
            l_idx, r_idx = data[i].index(token[0]), data[i].index(token[1])
            if l_idx == 4:
                tmp += data[i][0]
            else:
                tmp += data[i][l_idx + 1]
                
            if r_idx == 4:
                tmp += data[i][0]
            else:
                tmp += data[i][r_idx + 1]
            return tmp
                    

def col_check(token):
    for i in range(5):
        tmp = ""
        if token[0] in col_data[i] and token[1] in col_data[i]:
            l_idx, r_idx = col_data[i].index(token[0]), col_data[i].index(token[1])
            if l_idx == 4:
                tmp += col_data[i][0]
            else:
                tmp += col_data[i][l_idx + 1]
                
            if r_idx == 4:
                tmp += col_data[i][0]
            else:
                tmp += col_data[i][r_idx + 1]
            return tmp


def cross_check(token):
    l_idx = tmp_maps.index(token[0])
    r_idx = tmp_maps.index(token[1])
    l_i, l_j = l_idx // 5, l_idx % 5
    r_i, r_j = r_idx // 5, r_idx % 5
    return data[l_i][r_j] + data[r_i][l_j]


result = ""
for m in message:
    cur = row_check(m)
    if not cur:
        cur = col_check(m)
    if not cur:
        cur = cross_check(m)
    result += cur
print(result)
