def hanoi(n, source, target, spare):

    """ 
    Print all basic moves to be done in transferring n
    disks from the given source rod to the given target
    rod, involving the given pare rod to temporarily
    store disks.
    - Only one disk may be moved at a time, and no larger
    disk may ever be put on top of a smaller disk.
    """

    remaining_moves = [(n, source, target, spare)]
    curr_move = 0

    while curr_move < len(remaining_moves):
        curr_nb_disks,curr_source, curr_target, curr_spare =\
            remaining_moves[curr_move]
        
        if curr_nb_disks == 1:
            curr_move +=1
        else:
            # Replace the next move of n disks with the 3 steps
            # identified in the decomposition of the problem.
            remaining_moves[curr_move:curr_move+1] =\
                [ (curr_nb_disks-1, curr_source, 
                   curr_spare, curr_target),
                   (1, curr_source, curr_target, curr_spare),
                   (curr_nb_disks-1, curr_spare,
                   curr_target, curr_source)]

    return remaining_moves

assert hanoi(1, "S", "T", "X") ==\
    [(1, "S", "T", "X")]

assert hanoi(2, "S", "T", "X") ==\
    [(1, "S", "X", "T"),
    (1, "S", "T", "X"),
    (1, "X", "T", "S")]

assert hanoi(3, "S", "T", "X") ==\
    [(1, "S", "T", "X"),
    (1, "S", "X", "T"),
    (1, "T", "X", "S"),
    (1, "S", "T", "X"),
    (1, "X", "S", "T"),
    (1, "X", "T", "S"),
    (1, "S", "T", "X")]