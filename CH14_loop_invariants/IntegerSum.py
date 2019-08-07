def integer_sum(n):

    """ 
    Return the sum of the first n positive integer numbers.
    """

    sum = 0
    k = 0

    # INVARIANT
    #   The sum of far is equal to the sum of the first k integer numbers
    # VARIANT: n-k
    #
    while (k!=n):
        k += 1
        sum += k

    return sum

assert integer_sum(5) == 15