def is_sparse_vector(vector):
    """
      Check whether the given vector is a sparse vector.
      True if and only if the given vector is a dictionary,
      with keys as positive integer values, and values as
      non-zero numeric values, exept for the value at the 
      highest index which indicates the length of the vector.
    """

    if not isinstance(vector, dict):
        return False

    for key in vector:
        if (not isinstance(key, int)) or (key < 0):
            return False
        
        if (not isinstance(vector[key], (int, float))):
            return False

        if ( (vector[key] == 0) or vector[key] == 0.0) and\
            key < max(dict.keys(vector)):
            return False
    
    return True

assert is_sparse_vector({1:3, 6:12, 100:-67.9, 149:0})
assert is_sparse_vector({1:3, 6:12, 100:-67.9})
assert is_sparse_vector({0:0})
assert not is_sparse_vector({1:3, 6:0, 100:-67.9, 149:0})
assert not is_sparse_vector([1,2,3])

def length(vector):

    """
    Return the length of the given sparse vector.
    """
    return max(dict.keys(vector))+1


def vector_sum(left, right):
    """ 
    Compute the sum of two sparse vectors.
    The resulting vector also is a sparse vector,
    whose elements are the sum  of the elements at 
    corresponding positions in the given vectors.
    """

    if length(left) >= length(right):
        largest, smallest = left, right
    else:
        largest, smallest = right, left
    
    result = dict.copy(largest)

    for index in smallest:
        result[index] = \
            dict.get(largest, index, 0.0) + smallest[index]
        
        if (result[index]  == 0.0) and\
            (index < length(largest) - 1):
            del result[index]
    
    return result

vector1 = {4:2.3, 10:7.8, 23:9.9, 150:0.0}
vector2 = {1:4.2, 10:3.0, 112:10.0, 150:0.0}
assert vector_sum(vector1, vector2) == \
    {1:4.2, 4:2.3, 10:10.8, 23:9.9, 112:10.0, 150:0.0}

vector1 = {4:2.3, 10:0.0}
vector2 = {1:4.2, 20:10.0}
assert vector_sum(vector1, vector2) == \
    {1:4.2, 4:2.3, 20:10.0}

vector1 = {4:2.3, 10:7.8, 23:9.9, 150:0.0}
vector2 = {4:-2.3, 20:56.8, 160:0.0}
assert vector_sum(vector1, vector2) == \
    {10:7.8, 20:56.8, 23:9.9, 160:0.0}

vector1 = {4:2.3, 10:7.8, 23:9.9, 150:10.0}
vector2 = {4:-2.3, 10:-7.8, 23:-9.9, 150:-10.0}
assert vector_sum(vector1, vector2) == {150:0.0}