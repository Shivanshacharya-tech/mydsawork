#find maximum element in the given array

def find_maximum(arr, n):
    max_element= arr[0]
    for i in range(1,n):
        if arr[i]> max_element:
            max_element= arr[i]
    return max_element

