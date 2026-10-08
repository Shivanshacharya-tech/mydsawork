#maximum element of each row in the matrix

def maximum_element(matrix):
    max_elements= []
    for row in matrix:
        max_elements.append(max(row))
    return max_elements

if __name__ == "__main__":
    mat= [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result= maximum_element(mat)
    print(result)