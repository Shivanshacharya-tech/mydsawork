#min to max in array

t= int(input())

for i in range(t):
    n= int(input())
    arr= list(map(int,input().split()))
    m= min(arr)
    count_m = arr.count(m)
    operations= n- count_m
    print(operations)