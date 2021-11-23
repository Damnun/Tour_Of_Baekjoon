N = int(input()) # 사진틀 개수 (출력의 개수)
W = int(input()) # 총 추천 횟수
num = list(map(int, input().split())) # 추천 받은 리스트
photo = dict() # 사진틀

for i in range(W):
    if num[i] in photo: # 액자 안에 이미 학생이 있을 경우 추천수만 올려줌
        photo[num[i]][0] += 1
    else:
        if len(photo) < N: # 새로운 학생이 추가될 경우 (추천수 1, 들어온 순서)
            photo[num[i]] = [1, i]
        else:
            del_list = sorted(photo.items(), key= lambda x: (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[num[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
answer = str(ans_list[0])
for i in ans_list[1: ]:
    answer += " " + str(i)
print(answer)

***
딕셔너리 사용
학생 이름 : [추천 수, 추천 순서]
  0 ~ N 까지 loop -> i
  [
    추천리스트[i] = 학생 이름
    추천 순서 = i
  ]
  
  액자 수 초과시 딕셔너리의 추천수, 순서로 람다 정렬
  맨 처음 값(오름차순)을 키 값으로 본 값 제거.
  
  
  딕셔너리 자료형을 파이썬에서 처음 사용하다보니 실제 문제 풀이에서는 잘 떠오르지 않는다.
  처음에는 리스트에다가 학생 이름, 순서, 추천 수를 넣어서 루프 안에 루프를 넣어 매 번 구별하려 했지만
  생각대로 되지 않았다. 다중 우선순위로 풀 수도 있겠지만, 여러 복잡도상 딕셔너리를 사용하는게 제일 좋은 해답이었을 것 같다.
  열심히 공부하자..
  
***
