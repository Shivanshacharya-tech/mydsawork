#largest and second largest element in the given array

def largest_and_second_largest(arr, n):
    largest= second_largest= float('-inf')
    for i in range(n):
        if arr[i] > largest:
            second_largest= largest
            largest= arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest= arr[i]
    if second_largest == float('-inf'):
        return None
    return (largest, second_largest)
