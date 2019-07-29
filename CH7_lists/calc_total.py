def total(seq):
    """
    Return the total sum of all the elements in the
    given sequence.
    - The given sequence may only contain integer numbers
      and floating-point numbers
    """

    total_sum_so_far = 0

    for current_element in seq:
        total_sum_so_far += current_element

    return total_sum_so_far

assert total((1, 3, 5, 7)) == 16
assert total([]) == 0