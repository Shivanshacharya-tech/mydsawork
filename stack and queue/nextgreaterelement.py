#next greater element in the given stack

def next_greater_element(arr,n):
    stack= []
    result= [-1]*n
    for i in range(n):
        while stack and arr[stack[-1]]< arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

if __name__ == "__main__":
    arr= list(map(int,input().split()))
    n= len(arr)
    result= next_greater_element(arr,n)
    print(result)
    