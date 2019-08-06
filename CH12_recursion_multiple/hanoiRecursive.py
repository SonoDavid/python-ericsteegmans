def hanoi(n, source, target, spare):

    """ 
    Print all basic moves to be done in transferring n
    disks from the given source rod to the given target
    rod, involving the given pare rod to temporarily
    store disks.
    - Only one disk may be moved at a time, and no larger
    disk may ever be put on top of a smaller disk.
    """

    if n == 1:
        print('Move disk on top of', source, "to", target)
    else:
        hanoi(n-1, source, spare, target)
        print('Move disk on top of', source, "to", target)
        hanoi(n-1, spare, target, source)
