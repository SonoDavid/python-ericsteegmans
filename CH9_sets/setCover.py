def largest_common_set(sets, universe):
    """
        Return te smallest set in the given set of sets
        that has the most elements in common ith the given
        universe.
        - No other set in the set of sets has more elements
          in common wih the universe, and sets that have an
          equal number of elements in common with the
          universe have at least as many elements as the
          returned set.
    """

    largest_so_far = set()
    nb_largest_commons = 0

    for sett in sets:

        nb_current_commons = len(universe & sett)

        if (nb_current_commons > nb_largest_commons) or\
           ( (nb_current_commons == nb_largest_commons) and\
               (len(sett) < len(largest_so_far)) ):
            largest_so_far = sett
            nb_largest_commons = nb_current_commons

    return largest_so_far

assert largest_common_set(\
    {frozenset((1, 2, 5, 6)), frozenset((6, 7, 9)),\
        frozenset((1, 10, 8)), frozenset() },\
            {1, 2, 3, 4, 5, 6, 7, 8, 9})\
    == {1, 2, 5, 6}

assert largest_common_set(\
    {frozenset((1, 2, 3, 4, 5)), frozenset((1,3,5,7,9,11,13)) },\
    {1, 2, 3, 4, 5, 6, 7, 8, 9})\
    == {1, 2, 3,4, 5}

def cover_set(sets, universe):

    """
    Return a cover for the given universe involving
    sets of the given set of sets.
    - The returned cove is keps as small a posible
      without a guarantee that it is he smallest
      possible cover.
    """

    cover_so_far = set()
    sets_left = set.copy(sets)
    universe_left = set.copy(universe)

    while len(universe_left) > 0:
        next_set =\
            largest_common_set(sets_left, universe_left)
        set.add(cover_so_far, next_set)
        set.remove(sets_left, next_set)
        universe_left -= next_set

    return cover_so_far

assert cover_set(\
    { frozenset((1,2,3,4,5,6)), frozenset((6,7,9)),
    frozenset((1,10,8)), frozenset(("a","b","c"))},\
        {1,2,3,4,5,6,7,8,9})\
    == { frozenset((1,2,3,4,5,6)), frozenset((6,7,9)),
    frozenset((1,10,8))}