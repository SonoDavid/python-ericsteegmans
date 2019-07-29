from indexSmallest import index_smallest_of

def sort(lst):

    """ 
        Sort the elements of the given list in ascending
        order.
    """

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