#count sorted rows in the matrix

def count_sorted_rows(matrix):
    count = 0
    for row in matrix:
        if row == sorted(row):
            count += 1
    return count

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = count_sorted_rows(mat)
    print(result)
    