def matrix_product(matrix, vector):
    """
    Make a matrix product between a square matrix
    and a vector with the same dimension
    - This can be used in encryption cyphers
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    new_vector = [0] * n_rows
    for row in range(n_rows):
        for col in range(n_cols):
            new_vector[row]+= matrix[row][col] * vector[col]
    return new_vector


assert matrix_product([[-3, -3, -4], [0, 1, 1], [4, 3, 4]], [16, 18, 5])\
    == [-122, 23, 138]

assert matrix_product([[1, 0, 1], [4, 4, 3], [-4, -3, -3]], [-122, 23, 138])\
    == [16, 18, 5]