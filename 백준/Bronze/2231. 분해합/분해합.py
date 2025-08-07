N=int(input())


def digit_sum(x): #각 자리 수 합 구하는 함수
    total=0
    for i in str(x):
        total+=int(i)
    return total


d=len(str(N))
start=max(1,N-9*d)

for M in range(start,N):
    if M+digit_sum(M)==N:
        print(M)
        break
else:
    print(0)
