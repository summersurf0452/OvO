#난쟁이들의 전체 키의 합 구하기
arr=[int(input()) for _ in range(9) ]
sum_total=sum(arr)

#sum_total-( 2명 합 )==100 인 경우를 찾는것이 목표
#이중 for 문으로 순회하면서 모든 경우를 탐색한다

for i in range(9):
    for j in range(i+1,9):
        if arr[i]+arr[j]== sum_total-100:
            h1, h2=arr[i], arr[j]
            break #반복문 즉시 탈출하는 키워드
    else:
        continue # 이번턴에 못찾았으면 바깥 반복문 가서 다시 돌기

    break

#전체 리스트에서 난쟁이 2명을 빼고 정답 난쟁이들의 키만 출력하기

arr.remove(h1)
arr.remove(h2)

#오름차순 정렬하기
arr.sort()

for i in arr:
    print(i)
