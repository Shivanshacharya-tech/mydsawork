#factorial of largest number in the given array

def factorial(n):
    fact= 1
    for i in range(2, n+1):
        fact *= i
    ans= [int(ch) for ch in str(fact)]
    return ans

if __name__ == "__main__":
    n= 10
    print(factorial(n))
