def remove_duplicates(seq):
    """
    With while statements, change a list so that
    duplicate values inside of the list are removed. 
    The ordering of the list is kept
    """
    unique_len = len(set(seq))
    current_position = 0
    for current_position in range(unique_len):
        current_value = seq[current_position]
        tmp_seq = seq[current_position+1:]
        #print(seq)
        tmp_position = 0
        while tmp_position != len(tmp_seq):
            if tmp_seq[tmp_position] == current_value:
                del tmp_seq[tmp_position]
            else:
                tmp_position += 1
        seq[current_position+1:] = tmp_seq

# Assert the statement in textbook
lst = [7, 4, 12, 7, 1, 25, 7, 4, 0, 1, 20]
remove_duplicates(lst)
assert lst == [7, 4, 12, 1, 25, 0, 20]

# Assert other ordering close to each other
lst = [7, 7, 7, 4, 4, 12, 1, 1, 25, 0, 20]
remove_duplicates(lst)
assert lst == [7, 4, 12, 1, 25, 0, 20]