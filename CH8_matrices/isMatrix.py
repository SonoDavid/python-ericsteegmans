def is_matrix(matrix):

    """ 
    Check whether the given matrix is indeed a matrix.
    - True if and only if the given matrix is a non-empty
      sequence, whose elements are all sequences of the
      same length.
    """

    if not isinstance(matrix, (list, tuple)):
        return False
    if (len(matrix) == 0):
        return False

    nb_rows = len(matrix)
    nb_cols = None

    for row in range(nb_rows):

        if not isinstance(\
                matrix[row], (list, tuple, str, range)):
            return False

        if (nb_cols == None):
            nb_cols = len(matrix[row])
        elif (len(matrix[row]) != nb_cols):
            return False

    return True

assert is_matrix([[1]])
assert is_matrix(("abc", "123", "xyz"))
assert not is_matrix([])
assert not is_matrix([1, 2, 3])
assert not is_matrix(((1, 2, 3), ("a", "b"), (4, 5, 6)))