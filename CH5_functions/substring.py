def pos_leftmost_occ\
    (string, substring, start=0, end=None):

    """ 
        Return the start position of the leftmost occurrence
        of the given substring in the portion of the given
        string delimited by start and end.
        None is returned if no such occurrence can be found.
    """

    if end == None:
        end = len(string)
    
    result = None
    while (start < end-len(substring)+1) and\
        (result == None):
        if string[start:start+len(substring)] == substring:
            return start
        start += 1
