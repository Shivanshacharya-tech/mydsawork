#product of array with self

def productExceptSelf(nums):
    n = len(nums)
    result= [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                result[i] *= nums[j]
    return result

if __name__ == "__main__":
    nums= list(map(int, input().split()))
    result= productExceptSelf(nums)
    print(result)
    
