#rotate the matrix in clockwise direction

def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Transpose the matrix
    for i in range(n):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = rotate_matrix(mat)
    for row in result:
        print(row, end=" ")
    print()
    