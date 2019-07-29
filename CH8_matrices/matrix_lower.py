def is_lower_triangular(matrix):

    """ 
    Check whether the given square matrix is a lower
    triangular matrix.
    - A lower triangular matrix has no non-zero elements
      above the main diagonal.
    """

    for row in range(len(matrix)-1):
        for col in range(row+1, len(matrix[row])):
            if matrix[row][col] != 0:
                return False
        
    return True

matrix = [[22, 0, 0], [100, 200, 0], [0, 20, 33]]
assert is_lower_triangular(matrix)

matrix = [[22, 0, 1], [100, 200, 0], [0, 20, 33]]
assert not is_lower_triangular(matrix)

matrix = [ [22] ]
assert is_lower_triangular(matrix)