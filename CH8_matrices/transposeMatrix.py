def transpose(matrix):

    """ 
    Return the transpose of the given matrix.
    - The transpose of a matrix is obtained by writing
      the rows of the given matrix as the columns of the
      transpose.
    """

    nb_rows = len(matrix)
    nb_cols = len(matrix[0])
    result = [ [None]*nb_rows for k in range(nb_cols)]

    for row in range(nb_rows):
        for col in range(nb_cols):
            result[col][row] = matrix[row][col]
        
    return result

matrix = [ [22, 33, 44], [100, 200, 300] ]
assert transpose(matrix) == \
    [ [22, 100], [33, 200], [44, 300]]

matrix = [ [22] ]
assert transpose(matrix) == [[22]]