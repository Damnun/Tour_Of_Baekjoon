test_amount = int(input())
b = input().split()
score = []

for i in b:
    score.append(int(i))

max_score = max(score)
for i in range(len(score)):
    score[i] = score[i]/max_score*100

print(sum(score, 0.0) / len(score))
