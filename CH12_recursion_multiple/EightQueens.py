from Chess import get_column, is_under_attack_of

def eight_queens(given_positions=()):

    """
        Starting from a tuple of the given positions, return all
        possible positions of eight queens on a chessboard,
        such that no queen attacks another queen.
        - The given k positions are positions for the queens
          in the first k column
        - Queens at those positions do not attack each other
    """

    solutions = set()

    if len(given_positions) == 8:
        set.add(solutions, given_positions)

    else:
        
        curr_col = get_column(len(given_positions)+1)

        for row in range(1, 9):
            if not is_under_attack_of\
                ((curr_col, row),given_positions):
                set.update(solutions, 
                    eight_queens(given_positions+((curr_col, row),)))
    
    return solutions

def eight_queens_alt(given_positions=[]):

    """
        Starting from a tuple of the given positions, return all
        possible positions of eight queens on a chessboard,
        such that no queen attacks another queen.
        - The given k positions are positions for the queens
          in the first k column
        - Queens at those positions do not attack each other
    """

    solutions = set()

    if len(given_positions) == 8:
        set.add(solutions, tuple(given_positions))

    else:
        
        curr_col = get_column(len(given_positions)+1)

        for row in range(1, 9):

            curr_pos = (curr_col, row)

            if not is_under_attack_of\
                (curr_pos,given_positions):
                list.append(given_positions, curr_pos)
                set.update(solutions, 
                    eight_queens_alt(given_positions))
                list.remove(given_positions, curr_pos)

    return solutions

assert len(eight_queens()) == 92
assert len(eight_queens_alt()) == 92

assert\
    (("a", 8), ("b", 4), ("c", 1), ("d",3),
    ("e", 6), ("f", 2), ("g", 7), ("h", 5)) in eight_queens()
assert\
    (("a", 8), ("b", 4), ("c", 1), ("d",3),
    ("e", 6), ("f", 2), ("g", 7), ("h", 5)) in eight_queens_alt()