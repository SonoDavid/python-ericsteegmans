def get_column(nb=1):
    """
      Return the letter standing for the given column on a
      chessboard.
    """
    return chr(nb + ord("a") - 1)
    
def is_attacked_by(invest, attacker):
    """
      Check whether a queen at position invest on a 
      chesboard would be attacked by another queen at
      position attacker.
      - Positions are tuples starting with the letter of
        the column followed by the digit of the row.
    """

    # Same position?
    if (attacker == invest):
        return True

    # Same column?
    if (attacker[0] == invest[0]):
        return True

    # Same row?
    if (attacker[1] == invest[1]):
        return True

    if  abs(ord(attacker[0]) - ord(invest[0]))==\
            abs(attacker[1] - invest[1]):
        return True

    return False

def is_under_attack_of(invest, attackers):
    """ 
    Check whether a queen at position invest on a 
    chessboard would be attacked by at least one queen at
    a position in the given collection of positions
    attackers.
    """

    for pos in attackers:
        if is_attacked_by(invest, pos):
            return True
    
    return False