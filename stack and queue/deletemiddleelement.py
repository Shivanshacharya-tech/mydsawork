#delete middle element from stack and queue

def delete_middle_element(stack):
    n= len(stack)
    if n==0:
        return stack
    mid= n//2
    temp_stack= []
    for i in range(n):
        if i!= mid:
            temp_stack.append(stack[i])
    return temp_stack

if __name__ == "__main__":
    stack= list(map(int,input().split()))
    result= delete_middle_element(stack)
    print(result)
    