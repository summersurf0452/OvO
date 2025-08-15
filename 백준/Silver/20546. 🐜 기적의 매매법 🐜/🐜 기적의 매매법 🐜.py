#8/15

seed=int(input().strip())
#stock_price=[int(input()) for _ in range(10)]
stock_price=list(map(int,input().split()))
stock_num=0

#BNP

def junhyun(seed, available_stock, stock_num,stock_price):

    for ele in stock_price:
        if seed>=ele:
            available_stock=seed//ele
            stock_num+=available_stock
            seed-=available_stock*ele

    return seed+stock_num*stock_price[-1]



#TIMING
def sungmin(seed, available_stock, stock_num,stock_price):
    for i in range(3,len(stock_price)):
        if stock_price[i-3]< stock_price[i-2]<stock_price[i-1]:#3일간 상승
            seed+= stock_price[i]*stock_num
            stock_num=0
        elif stock_price[i-3] > stock_price[i-2]> stock_price[i-1]:  # 3일간 하락
            available_num=seed//stock_price[i]
            stock_num+=available_num
            seed-=available_num*stock_price[i]

    return seed+stock_num*stock_price[-1]

if junhyun(seed, 0, 0, stock_price) > sungmin(seed, 0, 0, stock_price):
    print("BNP")
elif junhyun(seed, 0, 0, stock_price) < sungmin(seed, 0, 0, stock_price):
    print("TIMING")
else:
    print("SAMESAME")


