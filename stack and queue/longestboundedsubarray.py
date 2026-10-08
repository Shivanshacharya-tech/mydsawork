#longest bounded subarray 

def longestSubarray(arr, x):
    
    n = len(arr)
    
    start = 0
    maxLen = 1
    
    for i in range(n):
        for j in range(i, n):
            
            # Find minimum and maximum elements
            mini = float('inf')
            maxi = float('-inf')
            
            for k in range(i, j + 1):
                mini = min(mini, arr[k])
                maxi = max(maxi, arr[k])
            
            # If difference is less than x,
            # compare length of subarray 
            if maxi - mini <= x and maxLen < j - i + 1:
                maxLen = j - i + 1
                start = i
    
    return arr[start: start + maxLen]

if __name__ == "__main__":
    arr = [8, 4, 5, 6, 7]
    x = 3

    res = longestSubarray(arr, x)
    
    print(*res)