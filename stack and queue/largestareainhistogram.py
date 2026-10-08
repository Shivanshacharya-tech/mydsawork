#largest area in the histogram

def getMaxArea(arr):
    res = 0
    n = len(arr)
    
    for i in range(n):
        curr = arr[i]
        
        # Traverse left while we have a greater height bar
        j = i - 1
        while j >= 0 and arr[j] >= arr[i]:
            curr += arr[i]
            j -= 1
        
        # Traverse right while we have a greater height bar
        j = i + 1
        while j < n and arr[j] >= arr[i]:
            curr += arr[i]
            j += 1
        
        res = max(res, curr)
    
    return res
    
if __name__ == "__main__":
    arr = [60, 20, 50, 40, 10, 50, 60]
    print(getMaxArea(arr))