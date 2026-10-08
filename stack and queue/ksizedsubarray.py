#k- sized  maximum subarray sum

def maxOfSubarrays(arr, k):
    n = len(arr)

    # to store the results
    res = []
  
    for i in range(0, n - k + 1):
      
        # Find maximum of subarray beginning
        # with arr[i]
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        res.append(max)
  
    return res

if __name__ == "__main__":
    arr = [ 1, 2, 3, 1, 4, 5, 2, 3, 6 ]
    k = 3
    res = maxOfSubarrays(arr, k)
    for maxVal in res:
        print(maxVal, end=" ")