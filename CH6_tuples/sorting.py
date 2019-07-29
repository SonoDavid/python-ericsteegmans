""" 
Assignment Chapter 6: Sorting
"""

def is_sorted(seq):
    """ Check is a sequence is sorted or not
    - Returns None is the length of the sequence is 0
    - Returns False if the sequence is not sorted
    - Returns True if the sequence is sorted
    """
    if len(seq) == 0:
        return None
    ind_small = 0
    ind_large = 1

    while ind_large < len(seq):
        if seq[ind_small] > seq[ind_large]:
            return False
        ind_small += 1
        ind_large += 1
    return True

assert is_sorted((0, 5, 15, 100)) == True
assert is_sorted((100, 15, 5, 2)) == False
assert is_sorted((0, 15, 5, 100)) == False
assert is_sorted((5,)) == True
assert is_sorted(()) == None

def get_ordering(seq):
    """ 
    Returns a string with the ordering of the sequence:
    - Returns ALL_EQUAL if the values are all equal
    - Returns ASCENDING if the values are ascending
    - Returns DESCENDING if the values are descending
    - Returns UNORDERED if the values are not ordered
    """
    ordered_up = is_sorted(seq)
    ordered_dn = is_sorted(seq[::-1])
    if ordered_up == None:
        return None
    if ordered_up == True and ordered_dn == True:
        return 'ALL_EQUAL'
    elif ordered_up == True:
        return 'ASCENDING'
    elif ordered_dn == True:
        return 'DESCENDING'
    else:
        return 'UNORDERED'
