N = int(input())
data = input()
result = ""

code = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
answer = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

count = 0
target = 0

for i in range(N):
    for j in range(8):
        for k in range(6):
            if data[target + k] == code[j][k]:
                count += 1
        if count >= 5:
            result += answer[j]
            count = 0
            break
        count = 0

    if len(result) != i+1:
        print(i + 1)
        exit()

    target += 6

print(result)

"""
입력 받은 코드 6자리와 코드표를 한자리씩 대조하여 일치할 경우 카운트를 늘려준다.
카운트가 5 이상일 경우 (즉 1개가 틀렸거나 전부 맞았을 경우) 해당 코드값을 딕셔너리 표로 보내 원하는 값을 뽑아낸다.
매 턴 정상적으로 실행된다면 결과값은 1개씩 증가해야 한다.
이를 어길 경우 코드에 오류가 있다는 뜻이므로 프로그램 종료후 인덱스 반환

딕셔너리 자료형을 연습해보았다.
"""
