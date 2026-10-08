#magic square of the matrix

def magic_square(n):
    if n < 3:
        return None

    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        i -= 1
        j += 1

        if num % n == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j == n:
            j = 0

    return magic_square


if __name__ == "__main__":
    n = int(input("Enter the size of the magic square (n >= 3): "))
    result = magic_square(n)
    if result is not None:
        for row in result:
            print(row)
    else:
        print("Magic square is not possible for n < 3.")
        