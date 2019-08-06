def quicksort(lst, low=0, high=None):
    """
    Sort the elements of the given list in the slice from
    low to high in ascending order
    """

    if high==None:
        high = len(lst)

    if low < high - 1:
         # The slice lst[low:high] has at least 2 elements
         index_of_pivot = partition(lst, low, high)
         quicksort(lst, low, index_of_pivot)
         quicksort(lst, index_of_pivot+1, high)

def partition(lst, low=0, high=None):
    """
    Partition the list in two parts:
    - Return the index of the pivot
    - All elements before the pivot are less then the pivot
    - All elements after the pivot are greater then or equal 
      to the pivot
    """
    if high == None:
        high = len(lst)

    pivot = (low+high)//2

    # Move the pivot to the start of the list
    lst[pivot], lst[low] = lst[low], lst[pivot]
    pivot = low

    for index in range(low + 1 , high):
        if lst[index] < lst[pivot]:
            element_at_index = lst[index]
            lst[index] = lst[pivot + 1]
            lst[pivot + 1] = lst[pivot]
            lst[pivot] = element_at_index
            pivot += 1
    return pivot

# Some test for the function quicksort
lst = []
quicksort(lst)
assert lst==[]

lst= [3]
quicksort(lst)
assert lst == [3]

lst = [3, -7, 6, -4, -11, 23, 2, 0]
quicksort(lst)
assert lst == [-11, -7, -4, 0, 2, 3, 6, 23]