#삼각수 목록 만들기
def triangle_num(n):
    return n*(n+1)//2


#가능한 모든 조합을 확인하는 코드

def is_triangle_num(x, arr):
    for i in arr:
        for j in arr:
            for k in arr:
                if i +j+k==x:
                    return True

    #모든 조합을 다 시도해본 뒤 못찾았을때 False 반환
    return False

Test_num=int( input())
arr1=[int(input().strip()) for _ in range(Test_num)]

limit=max(arr1)
arr2=[]
n = 1
while True:
    t = n * (n + 1) // 2
    if t > limit:
        break
    arr2.append(t)
    n += 1


for k in arr1:
    print(1 if is_triangle_num(k,arr2) else 0)