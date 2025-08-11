#8/11

from itertools import combinations

# 영햑이 카드 입력을 받는다

a,b= map(int, input().split())
yh_cards=[a,b]

# 전체 카드 리스트
all_cards=[]
for i in range(1,11):
    all_cards.extend([i,i])

# 영학이 카드 2개 제거

for i in yh_cards:
    all_cards.remove(i)

#족보 계산, 유형 나눠서 저장: 땡-2 끗-1

def ranking(card):
    x,y = card
    if x==y:
        return(2,x)
    else:
        return(1,(x+y)%10)

yh_rank=ranking(yh_cards)

#상대 카드와 영학이 카드 랭킹 비교, 승리 횟수 측정

win=0
total=0
for i in combinations(all_cards,2):
    others_rank= ranking(i)
    if yh_rank>others_rank:
        win+=1
    total+=1

#전체 확률 구하기. 소수점 셋째자리까지 출력해야하므로 .3f

answer=win/total
print(f"{answer:.3f}")
