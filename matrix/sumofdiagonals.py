#sum of diagonals of a given matrix

def sum_of_diagonals(matrix, n):
    primary_diagonal_sum= 0
    secondary_diagonal_sum= 0
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n-i-1]
    return (primary_diagonal_sum, secondary_diagonal_sum)

if __name__ == "__main__":
    n= int(input())
    matrix= []
    for i in range(n):
        row= list(map(int,input().split()))
        matrix.append(row)
    primary_sum, secondary_sum= sum_of_diagonals(matrix, n)
    print("Primary Diagonal Sum:", primary_sum)
    print("Secondary Diagonal Sum:", secondary_sum)
    