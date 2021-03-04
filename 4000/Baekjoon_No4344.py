case_amount = int(input())

for i in range(case_amount):
    cnt = 0  # 평균을 넘는 학생의 수를 저장
    test_case = []
    tmp_test_case = input().split()

    for j in tmp_test_case:
        test_case.append(int(j))

    avg = sum(test_case[1:]) / test_case[0]

    for j in range(len(test_case)):
        if j == 0:
            continue

        elif test_case[j] > avg:
            cnt += 1

    result = cnt / (len(test_case) - 1) * 100
    print("%.3f%%" % result)
