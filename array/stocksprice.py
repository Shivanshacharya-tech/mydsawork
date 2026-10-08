#best time to buy or sell stocks

def maxProfit(prices):
    n= len(prices)
    res=0

    for i in range(n-1):
        for j in range(i+1, n):
            res= max(res, prices[j]- prices[i])
    return res

if __name__ == "__main__":
    prices= list(map(int,input().split()))
    result= maxProfit(prices)
    print(result)