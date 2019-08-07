def find_longest_plateau(seq):

    """
    Return the index of the longest plateau in the given sequence.
    - A plateau is defined as a sequence of successive elements that are
      identical.
    """

    start_longest_so_far = 0
    length_longest_so_far = 0
    i = 0

    # INVARIANT
    #   The longest plateau in seq[0:i] starts at position
    #   start_longest_so_far and has a length of
    #   length_longest_so_far
    # VARIANT: len(seq) - i
    #
    while len(seq) - i > length_longest_so_far:

        length_current_plateau = length_plateau_at(seq, i)

        if length_current_plateau > length_longest_so_far:
            start_longest_so_far = i
            length_longest_so_far = length_current_plateau

        i += length_current_plateau

    return start_longest_so_far

def length_plateau_at(seq, start):

    """
    Return the length of the plateau starting at the given position in the
    given sequence.
    - All elements in seq[start:start+result] are equal, and either
      start+result is just beyond the last element of the sequence or
      the element at position start+result is different from the element
      at position start.
    """

    length = 1

    # INVARIANT
    #   All elements in seq[start:start+length] are equal.
    # VARIANT: len(seq) - length
    #
    while (start+length < len(seq)) and\
            (seq[start] == seq[start+length]):
        length += 1
    
    return length

assert find_longest_plateau((1,2,3,3,3,4,3,3)) == 2