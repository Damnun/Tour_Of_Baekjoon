from collections import Counter

n = int(input())
scores = []
total_score = [0] * n

# 대회 결과 저장
for _ in range(3):
    cur = list(map(int, input().split()))
    scores.append(cur)
    for i in range(n):
        total_score[i] += cur[i]
scores.append(total_score)

# 솔루션
for score in scores:
    score_counter = Counter(score)
    score_set = list(set(score))
    score_set.sort(reverse=True)
    score_dic = dict()
    
    token = 1
    for s in score_set:
        score_dic[s] = token
        token += score_counter[s]
        
    result = []
    for i in score:
        result.append(score_dic[i])
    print(*result)
