from indexSmallest import index_smallest_of

def sort(lst):

    """ 
        SELECTION SORT
        --------------
        Sort the elements of the given list in ascending
        order.
    """

    
    # INVARIANT
    # - All the elements in the given list at all handled positions
    #   are sorted in ascending order.
    # - All elements in the unhandled portion of the given list are all
    #   greater then or equal to all elements in the handled portion
    # - The given list is a permutation of the original list.
    # 
    for index_current in range(len(lst)-1):

        index_smallest = index_smallest_of(lst, index_current)

        lst[index_current], lst[index_smallest] = \
            lst[index_smallest], lst[index_current]

# Empty list
lst = []
sort(lst)
assert len(lst) == 0

# List with one element
lst = [20]
sort(lst)
assert (len(lst) == 1) and (lst[0] == 20)

# List with several elements
lst = [10, 20, -100]
lst2 = lst
sort(lst)
assert (len(lst) == 3) and (lst[0] == -100) and \
    (lst[1] == 10) and (lst[2] == 20)
assert lst is lst2