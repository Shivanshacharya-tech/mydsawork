#container with most water in an array

def max_water(arr):
    n= len(arr)
    res=0

    for i in range(n):
        for j in range(i+1, n):
            amount= min(arr[i], arr[j]) * (j-i)
            res= max(res, amount)
            return res

if __name__ == "__main__":
    arr= list(map(int,input().split()))
    result= max_water(arr)
    print(result)
    