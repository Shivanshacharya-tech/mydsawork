#common elements in two matrices

def common_elements(matrix1, matrix2):
    common = []
    for row1 in matrix1:
        for row2 in matrix2:
            for element1 in row1:
                for element2 in row2:
                    if element1 == element2 and element1 not in common:
                        common.append(element1)
    return common

if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matrix2 = [
        [5, 6, 7],
        [8, 9, 10]
    ]

    result = common_elements(matrix1, matrix2)
    print(result)
    