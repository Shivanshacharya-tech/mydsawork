#infix to postfix notation 

def infix_to_postfix(expression):
    precedence= {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack= []
    postfix= []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

if __name__ == "__main__":
    expression= "A+B*(C^D-E)^(F+G*H)-I"
    result= infix_to_postfix(expression)
    print("Postfix Notation:", result)
    