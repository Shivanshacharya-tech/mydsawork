#sum of maximum subarray of a given array

def sum_of_max_subarray(arr, n):
    max_sum= arr[0]
    current_sum= arr[0]
    for i in range(1,n):
        current_sum= max(arr[i], current_sum + arr[i])
        max_sum= max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    arr= list(map(int,input().split()))
    n= len(arr)
    result= sum_of_max_subarray(arr, n)
    print(result)
    