#two sum of the given array

def two_sum(arr, target):
    n= len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return True
            return False

    if __name__ == "__main__":
        arr= list(map(int,input().split()))
        target= int(input())
        result= two_sum(arr, target)
        if result:
            print("True")
        else:
            print("False")