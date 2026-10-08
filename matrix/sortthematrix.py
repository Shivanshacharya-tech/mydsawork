#sorting the matrix in row wise manner

def sort_matrix(matrix):
    for row in matrix:
        row.sort()
    return matrix

if __name__ == "__main__":
    mat = [
        [3, 1, 2],
        [6, 5, 4],
        [9, 8, 7]
    ]
    result = sort_matrix(mat)
    for row in result:
        print(row, end=" ")
    print()
    