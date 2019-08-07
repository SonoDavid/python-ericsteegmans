def nb_occurrences(element, sequence):

    """ 
    Return the number of occurenes of the given
    element in the given sequence.
    """

    nb_occurs = 0
    k = 0

    # INVARIANT
    #   nb_occurs stores the number of occurences of the given
    #   element in the slice sequence[0:k].
    # VARIANT: len(sequence) - k
    #   
    while k != len(sequence):

        if sequence[k] == element:
            nb_occurs += 1
        
        k += 1

    return nb_occurs

assert nb_occurrences('a',"aaaaarhus") == 5