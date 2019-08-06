def next_position(start_pos):
    if start_pos[1] >= 8:
        if start_pos[0] >= 8:
            return None
        else:
            return (start_pos[0]+1, 0)
    else:
        return (start_pos[0], start_pos[1]+1)

def get_value_at(grid, start_pos):
    return grid[start_pos[0]][start_pos[1]]

def set_value_at(grid, value, start_pos):
    grid[start_pos[0]][start_pos[1]] = value

def delete_value_at(grid, start_pos):
    grid[start_pos[0]][start_pos[1]] = None

def can_have_as_value_at(grid, value, start_pos):
    if value in grid[start_pos[0]]:
        return False
    if value in [row[start_pos[1]] for row in grid]:
        return False
    first_pos_col = ((start_pos[1]) // 3 * 3)
    first_pos_row = ((start_pos[0]) // 3 * 3)
    tot_block = grid[first_pos_row][first_pos_col:first_pos_col + 3]\
            + grid[first_pos_row + 1][first_pos_col:first_pos_col + 3]\
            + grid[first_pos_row + 2][first_pos_col:first_pos_col + 3]
    #import pdb; pdb.set_trace()
    if value in tot_block:
        return False
    return True

def fill(grid, start_pos=(0,0)):

    """ Fill the given grid completely in a blind way
    starting from the given position.
    - The function returns a bollean that indicates
      whether or not a complete fill was possible.
    """
    #import pdb; pdb.set_trace()

    if start_pos == None:
        return True
 
    elif get_value_at(grid, start_pos) != None:
        return fill(grid, next_position(start_pos))


    else:
        for value in range(1, 10):
            if can_have_as_value_at(grid, value, start_pos):
                set_value_at(grid, value, start_pos)
                if fill(grid, next_position(start_pos)):
                    return True
                delete_value_at(grid, start_pos)

list1 = [None, None, None, None, 3, None, None, None, 7]
list2 = [8, None, None, 2, None, None, None, 4, None]
list3 = [None, 6, 2, None, 4, None, None, 1, None]
list4 = [None, None, None, 9, None, 3, None, None, 8]
list5 = [None, 4, None, 6, None, None, None, None, None]
list6 = [9, None, None, None, None, None, 1, None, 6]
list7 = [None, None, None, 4, None, None, 8, None, None]
list8 = [None, 1, None, 8, None, 2, 9, None, None]
list9 = [None, 9, None, None, None, 1, None, 7, None]
matrix = [list1, list2, list3, list4, list5, list6, list7,
          list8, list9]
fill(matrix)
print(matrix)


