#snake pattern matrix

def snake_pattern(n):
    if n <= 0:
        return None

    matrix = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matrix[i][j] = num
                num += 1
        else:
            for j in range(n - 1, -1, -1):
                matrix[i][j] = num
                num += 1

    return matrix

if __name__ == "__main__":
    n = int(input("Enter the size of the snake pattern matrix: "))
    result = snake_pattern(n)
    if result is not None:
        for row in result:
            print(row)
    else:
        print("Invalid input. Please enter a positive integer.")
        