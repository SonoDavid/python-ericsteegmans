def extend_all(element, powerset):

    """
        Return a power set that has as its elements all the
        elements of the given power set extended with the
        given element.
    """

    new_elements = set()

    for subset in powerset:
        extended_element = subset | frozenset([element])
        set.add(new_elements, extended_element)
    
    return new_elements

assert extend_all(1, {}) == set()
assert extend_all(1, {frozenset()}) == {frozenset([1])}
assert extend_all(1, {frozenset(), frozenset({2, 3})}) ==\
    {frozenset({1}), frozenset({1,2,3})}

def power_set(sett):

    """ 
    Return the power set of the given sett.
    - The power set has as its elements all the subsets
      that can be formed with elements of the given sett.
    - Each element of the resulting set is a frozen set
      that contains elements of the given sett.
    """

    powerset_so_far = {frozenset()}

    for element in sett:
        set.update(powerset_so_far,\
            extend_all(element, powerset_so_far))
        
    return powerset_so_far

assert power_set(set()) == {frozenset()}
assert power_set({1}) == {frozenset(), frozenset({1})}
assert power_set({1, 2, 3}) ==\
    {frozenset(), frozenset({1}), frozenset({2}),
    frozenset({3}), frozenset({1, 2}),
    frozenset({1, 3}), frozenset({2, 3}),
    frozenset({1, 2, 3})}